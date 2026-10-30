"""Export a trained Neuron baseline as a portable state-dict bundle."""
from __future__ import annotations

import argparse
from pathlib import Path

import torch


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output", default="exports/neuron-byte-lm.pt")
    args = parser.parse_args()

    checkpoint = torch.load(args.checkpoint, map_location="cpu")
    if "model_state" not in checkpoint or "model_config" not in checkpoint:
        raise ValueError("checkpoint must contain model_state and model_config")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    bundle = {
        "format": "neuron-state-dict-v1",
        "model_config": checkpoint["model_config"],
        "model_state": checkpoint["model_state"],
        "training_step": checkpoint.get("step"),
    }
    torch.save(bundle, output)
    print(f"exported model bundle: {output}")


if __name__ == "__main__":
    main()
