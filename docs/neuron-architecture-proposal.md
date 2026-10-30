# Neuron Architecture Proposal

**Status:** Research proposal. This document records hypotheses and design options; it is not a description of implemented components.

## 1. Design objective

Neuron aims to become a general-purpose model that can continuously receive information, maintain an evolving internal state, and produce outputs while new inputs continue to arrive. The target is genuinely full-duplex behavior, not merely a conventional model wrapped in a streaming API.

The architecture should also investigate whether useful semantic representations can be learned through compression and experience rather than being fully prescribed by a fixed vocabulary.

## 2. Proposed conceptual pipeline

The following components are logical responsibilities. They need not become separate large neural networks.

1. **Modality adapters** convert raw or lightly processed inputs into modality-aware feature streams.
2. **Temporal/event interface** attaches ordering and timing information, supports partial chunks, and tracks stream state.
3. **Learned representation/compression** maps incoming features into compact, reusable latent units while preserving information needed for prediction and tasks.
4. **Shared multimodal workspace** exchanges information across modalities and maintains the active context.
5. **Memory system** stores selected experiences and consolidates recurring structure over longer timescales.
6. **Concurrent output heads** produce text, audio, or other outputs without requiring the input stream to stop.

A scheduler/runtime coordinates buffering, state updates, decoding, interruption, and backpressure. The runtime is part of the full-duplex system and must be measured alongside model compute.

## 3. Modality adapters

Use modality-appropriate front ends rather than forcing all raw data through one representation.

- **Text:** begin with UTF-8 byte input as a tokenizer-free baseline; later compare learned segmentation/compression against byte-only processing.
- **Audio:** investigate streaming acoustic features or learned codec representations with explicit timing.
- **Images/video:** investigate patch or frame representations and temporal grouping; raw byte input is not assumed to be efficient for visual data.
- **Other modalities:** add adapters only when there is a defined data source, task, and evaluation protocol.

Adapters should expose stable contracts: feature shape, timestamps, validity masks, stream identifiers, and state/reset semantics.

## 4. Learned information compression

The central hypothesis is that a model can learn compact intermediate information units that are reusable across contexts and potentially across modalities.

Candidate approaches to compare:

- continuous latent bottlenecks or learned slots;
- vector-quantized representations;
- hierarchical temporal chunking;
- predictive coding, where representations retain information needed to predict future observations;
- hybrid representations that preserve high-resolution detail only when required.

Possible objective terms include:
- reconstruction or sufficient-statistic preservation;
- next-event / future-feature prediction;
- downstream task loss;
- cross-modal consistency;
- rate or capacity regularization.

No single compression method is selected yet. Experiments must compare compression rate, reconstruction quality, downstream quality, latency, and memory use. A representation that compresses aggressively but discards information needed later is not a successful representation.

## 5. Full-duplex state and scheduling

A full-duplex implementation must handle overlapping streams explicitly.

Required behaviors to investigate:
- accept new input while output is being generated;
- update the active state from partial observations;
- allow new evidence to change, pause, or interrupt an output;
- preserve causal ordering and timestamps;
- handle dropped, delayed, or out-of-order chunks;
- bound queues and define backpressure behavior;
- distinguish temporary working state from persistent memory.

Evaluation should include time-to-first-response, streaming lag, interruption latency, synchronization error, and task quality under asynchronous input.

## 6. Memory hierarchy

Investigate at least three timescales:

- **Working state:** short-lived state required for the current interaction and streaming continuity.
- **Episodic memory:** selected events with temporal and contextual metadata.
- **Consolidated memory:** recurring patterns or stable information distilled from multiple episodes.

Memory must be selective. The system needs policies for write, update, retrieval, confidence, expiry, and correction. Evaluation should measure retrieval precision, stale-memory errors, storage growth, and the effect of memory on held-out tasks.

## 7. Training strategy

A staged curriculum is safer than attempting full-scale multimodal training immediately.

1. **Pipeline baseline:** verify byte-level text training, checkpointing, evaluation, and export.
2. **Representation experiments:** compare byte input and learned compression on controlled corpora.
3. **Streaming experiments:** train/evaluate on chunked sequences with variable arrival timing.
4. **Cross-modal experiments:** introduce paired modalities with explicit alignment and missing-modality tests.
5. **Memory experiments:** evaluate retrieval and consolidation on long-horizon tasks.
6. **Joint training:** combine streams, memory, and output generation only after component-level baselines are reproducible.

Training objectives should be ablated independently. Improvements must be measured against simple baselines.

## 8. Efficiency and deployment

The project should maintain configurations for multiple hardware budgets rather than assume one fixed deployment target.

Measure:
- parameter count and active parameters;
- peak allocated and reserved memory;
- tokens/bytes or frames per second;
- time-to-first-output and end-to-end latency;
- training throughput and total compute;
- quality at each model size.

Potential optimization areas include fused attention, activation checkpointing, mixed precision, grouped-query attention, selective context retention, quantization, and hardware-specific kernels. Each optimization must preserve a tested reference path and report quality/performance trade-offs.

A single RTX 3090-class GPU is a useful constraint for small-scale experiments and debugging. It should not be represented as sufficient for full 3B pretraining without a measured training plan.

## 9. Architecture decision process

For each major design decision, record:
- the problem and constraints;
- candidate approaches;
- expected benefits and failure modes;
- a small experiment that distinguishes the candidates;
- measured results and reproducibility details;
- the decision and conditions for revisiting it.

The architecture remains intentionally open until evidence supports a choice.
