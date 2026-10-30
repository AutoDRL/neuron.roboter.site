"""UTF-8 byte dataset for small language-model experiments."""
from __future__ import annotations

from pathlib import Path

import torch
from torch.utils.data import Dataset


class ByteTextDataset(Dataset[tuple[torch.Tensor, torch.Tensor]]):
    """Split a UTF-8 text file into fixed-length next-byte examples."""

    def __init__(self, path: str | Path, seq_len: int) -> None:
        if seq_len < 2:
            raise ValueError("seq_len must be >= 2")
        raw = Path(path).read_bytes()
        if not raw:
            raise ValueError(f"training text file is empty: {path}")
        values = [256, *raw, 257]
        self.tokens = torch.tensor(values, dtype=torch.long)
        self.seq_len = seq_len
        self.count = (len(self.tokens) - 1) // seq_len
        if self.count < 1:
            raise ValueError(
                f"dataset needs at least {seq_len + 1} tokens; got {len(self.tokens)}"
            )

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        if index < 0 or index >= self.count:
            raise IndexError(index)
        start = index * self.seq_len
        chunk = self.tokens[start : start + self.seq_len + 1]
        if chunk.numel() != self.seq_len + 1:
            raise RuntimeError("internal dataset chunk has an unexpected length")
        return chunk[:-1], chunk[1:]
