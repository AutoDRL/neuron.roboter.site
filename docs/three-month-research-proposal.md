# Neuron — Three-Month Research Proposal

**Status:** Draft for review; not submitted.  
**Project:** Neuron  
**Repository:** https://github.com/AutoDRL/neuron.roboter.site

## Summary

Neuron is an open research project exploring learned information compression, reusable representations, and continuous multimodal perception and generation. Its long-term goal is an efficient full-duplex multimodal model developed transparently for the research community.

The first funded phase will answer a narrower question: can learned compression improve the efficiency of streaming sequence representations without materially degrading prediction quality? This phase will build on the repository's small byte-level causal language-model baseline. It will not claim to train a frontier-scale model.

## Research questions

1. What information should compact learned representations preserve for prediction and downstream tasks?
2. How do continuous latent bottlenecks and learned temporal chunking compare?
3. What are the trade-offs among compression ratio, quality, latency, throughput, and memory?
4. How can representations be updated incrementally as input arrives in chunks?

## Three-month plan

### Month 1 — Baseline and evaluation
- Stabilize the byte-level training and evaluation pipeline.
- Add corpus-level train/validation/test splits and data provenance records.
- Define metrics for prediction quality, compression, throughput, peak memory, and streaming latency.

**Deliverables:** tested baseline, evaluation protocol, baseline report.

### Month 2 — Compression experiments
- Implement at least two comparable approaches, starting with a continuous latent bottleneck and learned temporal chunking.
- Run controlled experiments on documented, permissively licensed corpora.
- Measure quality, compression, latency, and memory trade-offs.

**Deliverables:** compression modules, experiment configs, reproducible ablations.

### Month 3 — Streaming prototype and release
- Connect the strongest candidate to an incremental sequence-processing prototype.
- Test variable chunk sizes, delayed input, and interrupted streams.
- Publish code, configurations, benchmark results, limitations, and a technical report.

**Deliverables:** streaming proof of concept and public research release.

## Compute request

Planning request: up to **2,000 H100-equivalent GPU-hours**, adjusted to the provider's hardware using measured throughput. Compute would support small-model training, compression ablations, streaming experiments, and reproducibility runs. This is a planning estimate, not a claim that a specific GPU type is interchangeable with another.

## Open outputs and public benefit

- Public source code and experiment configurations.
- Data manifests and licensing/provenance notes.
- Reproducible evaluation scripts and aggregate results.
- A technical report including negative results and limitations.

The work aims to make research on efficient learned representations and streaming models more inspectable and reproducible for independent developers.

## Current state

The repository currently contains a small byte-level causal text-model baseline, basic training/validation/export scripts, initial tests, and architecture documents. It does not yet contain a trained 3B model, a completed full-duplex system, a multimodal training pipeline, or published benchmark results.

## Applicant review required

Before submission, the applicant must personally verify eligibility, identity and contact details, biography, prior-work evidence, and the funder's payment/tax requirements. Sensitive personal, tax, or banking information must only be provided directly through a funder's secure process, never in this public repository.
