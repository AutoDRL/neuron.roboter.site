"""Small byte-level causal Transformer baseline.

This is an engineering baseline for validating the training pipeline. It is
not the final Neuron full-duplex or multimodal architecture.
"""
from __future__ import annotations

import torch
from torch import nn
from torch.nn import functional as F


class ByteLanguageModel(nn.Module):
    """Autoregressive byte model with reserved BOS and EOS IDs.

    UTF-8 bytes use IDs 0..255; BOS=256 and EOS=257.
    """

    BOS_ID = 256
    EOS_ID = 257

    def __init__(
        self,
        vocab_size: int = 258,
        d_model: int = 256,
        n_heads: int = 4,
        n_layers: int = 4,
        max_seq_len: int = 256,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        if vocab_size < 258:
            raise ValueError("vocab_size must be at least 258 (bytes + BOS/EOS)")
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        if n_layers < 1 or max_seq_len < 2:
            raise ValueError("n_layers must be >= 1 and max_seq_len >= 2")

        self.vocab_size = vocab_size
        self.max_seq_len = max_seq_len
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.position_embedding = nn.Embedding(max_seq_len, d_model)
        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=4 * d_model,
            dropout=dropout,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.transformer = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.final_norm = nn.LayerNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)
        self.lm_head.weight = self.token_embedding.weight
        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        input_ids: torch.Tensor,
        targets: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        if input_ids.ndim != 2:
            raise ValueError("input_ids must have shape [batch, sequence]")
        batch_size, seq_len = input_ids.shape
        if seq_len > self.max_seq_len:
            raise ValueError(
                f"sequence length {seq_len} exceeds max_seq_len={self.max_seq_len}"
            )

        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        x = self.token_embedding(input_ids) + self.position_embedding(positions)
        x = self.dropout(x)
        causal_mask = torch.triu(
            torch.ones(seq_len, seq_len, device=input_ids.device, dtype=torch.bool),
            diagonal=1,
        )
        x = self.transformer(x, mask=causal_mask)
        logits = self.lm_head(self.final_norm(x))

        loss = None
        if targets is not None:
            if targets.shape != input_ids.shape:
                raise ValueError("targets must have the same shape as input_ids")
            loss = F.cross_entropy(
                logits.reshape(batch_size * seq_len, self.vocab_size),
                targets.reshape(batch_size * seq_len),
            )
        return logits, loss

    @torch.no_grad()
    def generate(
        self,
        input_ids: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
    ) -> torch.Tensor:
        if temperature <= 0:
            raise ValueError("temperature must be positive")
        if max_new_tokens < 0:
            raise ValueError("max_new_tokens must be non-negative")
        was_training = self.training
        self.eval()
        try:
            for _ in range(max_new_tokens):
                context = input_ids[:, -self.max_seq_len :]
                logits, _ = self(context)
                next_logits = logits[:, -1, :] / temperature
                if top_k is not None:
                    if top_k < 1:
                        raise ValueError("top_k must be >= 1")
                    k = min(top_k, next_logits.size(-1))
                    threshold = torch.topk(next_logits, k).values[:, -1, None]
                    next_logits = next_logits.masked_fill(
                        next_logits < threshold, float("-inf")
                    )
                probabilities = F.softmax(next_logits, dim=-1)
                next_token = torch.multinomial(probabilities, num_samples=1)
                input_ids = torch.cat((input_ids, next_token), dim=1)
        finally:
            self.train(was_training)
        return input_ids
