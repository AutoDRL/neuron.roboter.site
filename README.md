# Neuron

**Neuron** is an open research project exploring a from-scratch, full-duplex, multimodal general-purpose language model.

The project investigates real-time perception and generation across modalities, learned information compression, reusable representations, and long-term memory.

> **Status:** Initial repository setup and architecture research. The capabilities described here are research goals, not claims of completed implementation.

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

Directories and entry points will be added as implementation begins; this describes the intended organization.

## Current status

- [x] Repository created
- [x] Initial project overview published
- [ ] Publish detailed architecture specification
- [ ] Establish data and evaluation principles
- [ ] Implement minimal runnable training baseline
- [ ] Validate memory and throughput on target hardware
- [ ] Publish reproducible experiments
- [ ] Expand multimodal and full-duplex capabilities

## Open collaboration

Neuron is intended to be developed transparently with contributors worldwide. Contributions should include reproducible experiments, clear documentation, and a careful distinction between demonstrated results and future plans.

No license has been added yet. Until a license is explicitly selected and published, do not assume the code is licensed for reuse.
