"""Train the initial byte-level Neuron baseline."""
from __future__ import annotations

import argparse
from pathlib import Path

import torch
from torch.utils.data import DataLoader, random_split

from dataset.byte_text import ByteTextDataset
from modules.byte_lm import ByteLanguageModel
from solvers.optim import build_adamw
from toolkit.config import load_config, set_seed


def evaluate(model, loader, device, max_batches: int) -> float:
    model.eval()
    losses = []
    with torch.no_grad():
        for batch_index, (inputs, targets) in enumerate(loader):
            if batch_index >= max_batches:
                break
            _, loss = model(inputs.to(device), targets.to(device))
            losses.append(float(loss.item()))
    model.train()
    if not losses:
        raise RuntimeError("validation loader produced no batches")
    return sum(losses) / len(losses)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/byte_lm_tiny.json")
    parser.add_argument("--data", required=True, help="UTF-8 text corpus path")
    args = parser.parse_args()

    config = load_config(args.config)
    model_cfg = config["model"]
    train_cfg = config["training"]
    set_seed(int(train_cfg.get("seed", 1337)))

    dataset = ByteTextDataset(args.data, int(model_cfg["max_seq_len"]))
    if len(dataset) < 2:
        raise ValueError("at least two sequence chunks are required for train/validation split")
    val_size = max(1, int(len(dataset) * 0.1))
    train_size = len(dataset) - val_size
    train_set, val_set = random_split(
        dataset,
        [train_size, val_size],
        generator=torch.Generator().manual_seed(int(train_cfg.get("seed", 1337))),
    )
    batch_size = int(train_cfg["batch_size"])
    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, drop_last=False)
    val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=False, drop_last=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ByteLanguageModel(**model_cfg).to(device)
    optimizer = build_adamw(
        model,
        float(train_cfg["learning_rate"]),
        float(train_cfg.get("weight_decay", 0.1)),
    )

    output_dir = Path(train_cfg.get("output_dir", "runs/byte_lm_tiny"))
    output_dir.mkdir(parents=True, exist_ok=True)
    max_steps = int(train_cfg["max_steps"])
    eval_interval = max(1, int(train_cfg.get("eval_interval", 100)))
    eval_batches = max(1, int(train_cfg.get("eval_batches", 20)))
    iterator = iter(train_loader)

    print(f"device={device} train_sequences={train_size} val_sequences={val_size}")
    model.train()
    for step in range(1, max_steps + 1):
        try:
            inputs, targets = next(iterator)
        except StopIteration:
            iterator = iter(train_loader)
            inputs, targets = next(iterator)

        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad(set_to_none=True)
        _, loss = model(inputs, targets)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        if step == 1 or step % eval_interval == 0 or step == max_steps:
            val_loss = evaluate(model, val_loader, device, eval_batches)
            print(f"step={step}/{max_steps} train_loss={loss.item():.4f} val_loss={val_loss:.4f}")
            checkpoint = {
                "model_state": model.state_dict(),
                "model_config": model_cfg,
                "training_config": train_cfg,
                "step": step,
                "validation_loss": val_loss,
            }
            torch.save(checkpoint, output_dir / "checkpoint.pt")
            model.train()

    print(f"saved checkpoint: {output_dir / 'checkpoint.pt'}")


if __name__ == "__main__":
    main()
