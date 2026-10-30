# Neuron

**Neuron** is an open research project exploring a from-scratch, full-duplex, multimodal general-purpose language model.

The project investigates real-time perception and generation across modalities, learned information compression, reusable representations, and long-term memory.

> **Status:** The repository now contains an initial byte-level text-model baseline and a basic training/validation/export pipeline. These are engineering foundations, not the final full-duplex multimodal architecture.

## Research goals

- Full-duplex interaction: concurrent perception and generation.
- Multimodal representation: shared and modality-specific representations for text, audio, images, and other signals.
- Learned information compression: compact, reusable information units learned from low-level inputs.
- Memory and consolidation: retaining, combining, and reusing information over time.
- Efficient training and inference across different hardware budgets.

## Initial engineering targets

- Python 3.10+
- PyTorch 2.0+
- Native, inspectable implementations where practical
- Modular training, validation, and export entry points
- Hardware-aware configurations, including a single-GPU development path

The initial research target includes a 3B-parameter model, subject to feasibility studies, data availability, and compute funding. This is a target, not a completed model.

## Quick start

Install the package and development tools:

```bash
python -m pip install -e ".[dev]"
```

Train the tiny byte-level baseline on a UTF-8 text corpus:

```bash
python trainer.py --config configs/byte_lm_tiny.json --data /path/to/corpus.txt
```

See [the baseline guide](docs/byte-baseline.md) for validation, export, tests, and known limitations.

## Intended repository layout

```text
.
├── configs/       # Model and experiment configurations
├── dataset/       # Data preparation and input pipelines
├── docs/          # Architecture, research notes, and roadmap
├── modules/       # Model components and optimized operators
├── solvers/       # Optimizers, losses, and training components
├── toolkit/       # Shared utilities, I/O, and parsing
├── trainer.py     # Unified training entry point
├── valider.py     # Unified validation entry point
└── exports.py     # Model export entry point
```

## Current status

- [x] Repository and project overview
- [x] Initial byte-level causal-LM baseline
- [x] Basic training, validation, and export entry points
- [x] Initial unit tests and CI workflow
- [x] Baseline usage and limitation documentation
- [ ] Run and record local/CI test results
- [ ] Establish corpus-level data provenance and evaluation protocol
- [ ] Develop streaming full-duplex architecture
- [ ] Research learned cross-modal compression and memory
- [ ] Benchmark hardware and optimize kernels

## Open collaboration

Neuron is intended to be developed transparently with contributors worldwide. Contributions should include reproducible experiments, clear documentation, and a careful distinction between demonstrated results and future plans.

No license has been added yet. Until a license is explicitly selected and published, do not assume the code is licensed for reuse.
