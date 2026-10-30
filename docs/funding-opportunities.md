# Neuron Funding and Compute Strategy

**Last checked:** 2026-10-30  
**Status:** Research notes. No application has been submitted and no award is implied.

## 1. Priority order

### A. fal Research Grants — compute-first

Official page: https://fal.ai/grants

- The program provides free compute resources for researchers and developers working on open-source AI.
- The official page says the average grant check is $50,000; this is a program-level average, not a guaranteed award or a fixed entitlement.
- The application route is email to grants@fal.ai.
- The request should describe the project, goals, open-source alignment, and relevant work or repository links.

**Neuron fit:** High for GPU/compute support. The application should request a bounded experiment with a clear GPU-hour budget, training plan, deliverables, and public results. The current baseline is a starting point; do not describe a full multimodal model as already implemented.

### B. RAAIS Foundation Grants — three-month public-benefit project

Official page: https://www.raais.org/grants/

- Supports open-source AI research and projects worldwide.
- Each grant supports a defined three-month project.
- Applications are rolling.
- The foundation explicitly aims to support individuals and communities that may lack resources.
- Applications are submitted through the form embedded on the official grants page.

**Neuron fit:** High if the proposal is scoped to a concrete three-month public research output, such as a reproducible learned-compression experiment or an open streaming multimodal prototype. The exact award size and payment/tax arrangements are not published on the grants page and must be confirmed with the foundation before relying on personal payment.

### C. AI Grant — open-source grant and cluster compute

Official pages:
- https://aigrant.org/
- https://new.aigrant.org/

The two official pages currently show different grant ranges:
- The original page lists $5,000–$50,000, in cash or compute.
- The newer page lists $10,000–$100,000 and compute grants on the Andromeda Cluster.

The newer page also contains a separate, old startup SAFE/accelerator offer. That investment offer is not the same as a non-dilutive open-source grant and should not be selected for this project.

**Neuron fit:** High. Apply specifically to the open-source grant/compute track. Confirm the current amount, eligible recipient, permitted compute use, and payment mechanism in the live application form before submitting.

### D. Mozilla Foundation 2027 Fellowships — individual research support

Official call and FAQ:
- https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/
- https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/faqs/

- The 2027–2028 fellowship is for individuals.
- Independent Fellows may receive a $100,000 stipend plus a $25,000 project budget.
- The Letter of Intent deadline is December 17, 2026 at 11:59 PM Pacific (UTC-8).
- Relevant themes include sovereign AI, public infrastructure and maintenance, hard infrastructure/compute, and wildcards.
- Applicants must be legally able to receive grant funds from a U.S.-based 501(c)(3) organization and the project must have a charitable purpose.
- The program expects technical ability, a credible record of building, and a deliverable project.

**Neuron fit:** Potentially strong only if the proposal focuses on open, community-benefiting sovereign AI infrastructure and a concrete 12-month deliverable. This is not a generic request to fund a large model. The applicant must personally review and author the final application in their own voice; AI assistance is limited to supportive uses.

### E. Sequoia Open Source Fellowship — revisit after adoption

Official page: https://sequoiacap.com/oss

- Supports open-source creators and projects with real-world adoption.
- No company is required and no equity is taken.
- The stipend is intended to cover reasonable living expenses for 6–12 months.
- The program is rolling and selective.

**Neuron fit:** Lower at the current stage. Revisit after the repository has a working release, external contributors or users, and evidence of adoption. The stipend is not a dedicated GPU-credit award.

## 2. Not a current priority

### Mozilla Human-Scale AI Incubator

Official call: https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/

The current incubator seeks working technologies already deployed with intended users and evidence of product-community fit. It is not designed for a project that is currently only an early model-development repository. Reassess only after Neuron has a real use case, pilot users, and community feedback.

### OpenMined Winter 2026 grant

Official page: https://openmined.org/research/grants/

The current call is focused on ensembles, routing, and model composition, with a deadline of October 30, 2026. It is not aligned with Neuron's present from-scratch pretraining and architecture work, so it is not a priority application.

## 3. Common application evidence to prepare

- Public repository and a clear statement of current implementation status.
- A concise technical proposal with one primary research question.
- Three-month milestones and measurable deliverables.
- Compute budget: GPU type, GPU-hours, storage, data pipeline, checkpointing, and expected experiments.
- Data provenance, licensing, and evaluation protocol.
- Open-source contribution and publication plan.
- A truthful maintainer biography and prior-work evidence supplied by the applicant.
- Recipient, tax, and payment eligibility confirmed for the applicant's country of residence.

## 4. Submission integrity

No funding application should claim that Neuron has completed full-duplex multimodal training, achieved benchmark results, or trained a 3B model. Those remain goals. The first baseline currently in the repository is a small byte-level causal text model used to validate the engineering pipeline.

Do not submit an application, accept terms, provide tax/banking data, or make legal representations on the applicant's behalf without the applicant's review and explicit approval.
