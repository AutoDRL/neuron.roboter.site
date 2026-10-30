import torch

from modules.byte_lm import ByteLanguageModel


def make_model():
    return ByteLanguageModel(
        vocab_size=258,
        d_model=32,
        n_heads=4,
        n_layers=2,
        max_seq_len=16,
        dropout=0.0,
    )


def test_forward_and_loss():
    model = make_model()
    tokens = torch.randint(0, 258, (2, 8))
    logits, loss = model(tokens, tokens)
    assert logits.shape == (2, 8, 258)
    assert loss is not None
    assert torch.isfinite(loss)
    loss.backward()


def test_causal_mask_prevents_future_token_leakage():
    torch.manual_seed(7)
    model = make_model().eval()
    first = torch.tensor([[1, 2, 3, 4]])
    changed_future = torch.tensor([[1, 2, 99, 100]])
    with torch.no_grad():
        logits_a, _ = model(first)
        logits_b, _ = model(changed_future)
    torch.testing.assert_close(logits_a[:, :2], logits_b[:, :2])


def test_generate_appends_requested_number_of_tokens():
    model = make_model()
    prompt = torch.tensor([[256, 65, 66]])
    result = model.generate(prompt, max_new_tokens=3, temperature=1.0, top_k=8)
    assert result.shape == (1, 6)
