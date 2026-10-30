# Byte-Level Baseline: Quick Start

This baseline exists to validate the repository's data, model, optimization, training, validation, and export path. It is deliberately small and is **not** the final Neuron architecture.

## Environment

- Python 3.10+
- PyTorch 2.0+
- Optional: pytest for tests

Install the project:

```bash
python -m pip install -e ".[dev]"
```

## Prepare data

Provide a UTF-8 plain-text corpus. The loader encodes the file as raw UTF-8 bytes and adds reserved beginning/end markers. Do not commit private, copyrighted, or otherwise restricted datasets to the repository.

The initial loader makes fixed-length chunks. For meaningful experiments, document the corpus source, license, preprocessing, and train/validation split.

## Train

```bash
python trainer.py --config configs/byte_lm_tiny.json --data /path/to/corpus.txt
```

The script selects CUDA when available and otherwise uses CPU. It writes a checkpoint under the configured output directory (default: `runs/byte_lm_tiny/checkpoint.pt`).

The included tiny configuration is for smoke tests and early experiments. It is not a recommended production configuration and does not represent a 3B model.

## Validate

```bash
python valider.py --checkpoint runs/byte_lm_tiny/checkpoint.pt --data /path/to/held-out-corpus.txt
```

Use a genuinely held-out corpus for final evaluation. The trainer's initial random chunk split is only a pipeline smoke-test split and may not be suitable for rigorous scientific reporting.

## Export

```bash
python exports.py --checkpoint runs/byte_lm_tiny/checkpoint.pt --output exports/neuron-byte-lm.pt
```

The exported bundle contains the model configuration and PyTorch state dictionary.

## Tests

```bash
pytest
```

## Known limitations

- This is a byte-level autoregressive text baseline, not a full-duplex model.
- It does not yet implement audio/image encoders, streaming synchronization, learned latent compression, or persistent memory.
- It uses PyTorch's standard Transformer encoder layers; optimized attention kernels and hardware-specific backends have not yet been integrated or benchmarked.
- The current random train/validation chunk split is for pipeline verification only. Scientific evaluation requires a corpus-level held-out split and documented dataset provenance.
- No model quality, training speed, or hardware efficiency claims are made until reproducible measurements are published.
