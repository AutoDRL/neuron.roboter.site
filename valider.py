"""Evaluate a saved Neuron baseline checkpoint."""
from __future__ import annotations

import argparse

import torch
from torch.utils.data import DataLoader

from dataset.byte_text import ByteTextDataset
from modules.byte_lm import ByteLanguageModel


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model = ByteLanguageModel(**checkpoint["model_config"]).to(device)
    model.load_state_dict(checkpoint["model_state"])
    model.eval()

    dataset = ByteTextDataset(args.data, int(checkpoint["model_config"]["max_seq_len"]))
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False)
    losses = []
    with torch.no_grad():
        for inputs, targets in loader:
            _, loss = model(inputs.to(device), targets.to(device))
            losses.append(float(loss.item()))
    if not losses:
        raise RuntimeError("validation dataset produced no batches")
    mean_loss = sum(losses) / len(losses)
    perplexity = float(torch.exp(torch.tensor(mean_loss)).item())
    print(f"validation_loss={mean_loss:.6f} perplexity={perplexity:.4f} batches={len(losses)}")


if __name__ == "__main__":
    main()
