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


## 5. Applicant location and cross-border eligibility (checked 2026-10-30)

The applicant has identified Shanghai, China as the current legal residence. San Francisco, United States is a possible alternative location, but it must not be represented as the applicant's residence unless it is genuinely the primary place of residence during the relevant grant/fellowship period and the applicant has the required lawful status and payment arrangements.

### Location-specific findings

- **fal Research Grants:** The official page says the program is open to anyone passionate about open-source AI and does not publish a country exclusion list. It asks applicants to email grants@fal.ai. China eligibility is therefore not expressly ruled out by the public page, but the grants team should confirm any export-control, account, and service availability restrictions before a compute plan is finalized. Do not treat the $50,000 average grant check shown on the page as an entitlement or a guaranteed compute allocation.
- **RAAIS Foundation Grants:** The official grants page explicitly describes support for open-source AI projects worldwide and rolling three-month project grants. The public page does not state a country exclusion list or individual payment rules. An applicant based in Shanghai should ask the foundation to confirm whether it can contract with and pay an individual resident in mainland China, including the available payment rail and any tax documentation.
- **AI Grant:** The original open-source grants page lists $5,000–$50,000 in cash or compute. The newer page advertises $10,000–$100,000 and Andromeda compute, but also contains a distinct startup-investment offer whose terms are not a non-dilutive grant. Neither public page clearly states a China-specific eligibility rule. Ask the grant team to confirm current program status, recipient-country eligibility, compute access from mainland China, and whether the requested support is a grant rather than an investment.
- **Mozilla 2027 Fellowship:** The official FAQ says applicants must be individuals and must be legally able to receive funding from a U.S.-based 501(c)(3). The live Letter of Intent form asks for current location and says the primary location should be where the applicant will reside during the Fellowship if they live in more than one place; it also contains a location-based funding eligibility gate. The public materials reviewed do not establish that a Shanghai-based applicant is eligible or ineligible by country alone. Before investing substantial effort, verify the exact country/location eligibility in the live form and with Mozilla. Do not enter San Francisco unless it is genuinely the applicant's primary location during the Fellowship and the applicant can lawfully reside and receive funds there.
- **Sequoia Open Source Fellowship:** Keep as a later-stage option after Neuron has external users, contributors, or demonstrable adoption; confirm country/payment eligibility if and when applying.

### Practical application rule

Use Shanghai, China as the applicant location unless the applicant confirms a genuine change in primary residence for the relevant period. A collaborator, mailing address, VPN endpoint, company formation location, or willingness to travel to San Francisco does not by itself establish U.S. residence or U.S. work authorization. Do not use another person's address, bank account, or legal entity as a workaround. Confirm country eligibility and payment rails with each funder in writing before submitting legal or financial declarations.


## 6. China-based opportunities and revised priority (checked 2026-10-30)

The applicant's current legal residence is Shanghai, China. U.S. residence-based routes are not part of the current plan. Prioritize routes that either explicitly welcome worldwide applicants or are available through eligible mainland-China institutions/communities. "No country exclusion stated" is not the same as confirmed approval for a mainland-China recipient; confirm account access, contracting, export-control, payment, and tax details with the funder.

### Priority 1 — fal Research Grants (compute)

Official page: https://fal.ai/grants

The current official page says the program is open to anyone advancing AI through open-source projects, requires no formal degree, and provides free compute. It asks applicants to email grants@fal.ai with the project description, goals, open-source fit, and relevant work/GitHub links. It does not publish a country exclusion list on the page. This is the strongest direct compute-first route to test from Shanghai, subject to written confirmation that a mainland-China-based recipient can access the awarded services and comply with provider terms. The displayed $50,000 average grant check is not a guaranteed amount or promise to an individual applicant.

### Priority 2 — RAAIS Foundation Grants (three-month research grant)

Official page: https://www.raais.org/grants/

The foundation explicitly says it supports open-source AI research and projects worldwide, accepts rolling applications, and funds defined three-month projects. It particularly aims to support individuals and communities with limited resources. The public page does not disclose a country list, award size, or detailed personal-payment mechanism. Ask whether an individual legally resident in mainland China can be the grantee and how funds can be paid and documented. A suitable Neuron proposal should focus on one bounded, measurable public research result rather than requesting general funding for a large model.

### Priority 3 — China Youth Open Source Seed Fund (small domestic project grant)

Announcement: https://www.ccf.org.cn/Media_list/cncc/2026-10-17/940916.shtml

A CCF article dated October 17, 2026 reports a Youth Open Source Special Fund Seed Program jointly associated with CCF's Open Source Development Technical Committee, Mulan Open Source Community, QI-WU Learning Community, AI Infra Open Source Community, MuXi, and China Guanghua Science and Technology Foundation. It says individual developers and teams may apply; selected projects receive funding and ecosystem support. The second application batch deadline is October 31, 2026. The article reports RMB 4,000 for basic-level projects and RMB 12,000 for key-level projects. AI Infra is an explicit focus, making this thematically relevant to Neuron, but the currently published examples emphasize domestic AI infrastructure and ecosystem adaptation. Confirm the actual application form, applicant age/identity rules, project scope, and submission method immediately; do not assume the CCF article alone constitutes a complete application guide. This is a small seed grant, not meaningful 3B-model GPU funding.

### Conditional route — Huawei Cloud AI 100 Schools 2.0 (Ascend compute)

Official page: https://developer.huaweicloud.com/homepage/aiinnovation.html

The official page supports Ascend cloud AI compute for research innovation, including model training. However, the applicant must be a currently enrolled student/teacher at a nationally recognized university or a staff member of a research institution, must join Huawei's developer program, show substantial AI research achievements, and submit a project explicitly planned for the Ascend platform. It is therefore only viable if the applicant meets the institutional-affiliation requirement. The page says individual applications are for teachers/students; it does not create a general independent-developer route. Compute support is reviewed competitively and is restricted to non-commercial use.

### Institutional-only route — China Science and Technology Development Foundation "Compute Without Borders" 2026

Official announcement: https://fdstmc.cast.org.cn/xwdt/tzgg/art/2026/art_05fa2ffb94ae4b6eb5f81e9fa84a2fa7.html

The October 16, 2026 announcement describes donated high-performance CPU core-hours, with up to one million core-hours per selected institution. Eligible applicants are universities, research institutes, and specified new-technology enterprises; applications must be submitted by the institution, not an individual. Although AI model training is among supported areas, this is CPU supercomputing capacity rather than a direct GPU grant. Consider only if Neuron can work with an eligible institution and the institution can lawfully use the resource for the project.

### Lower priority / monitor

- **Swiss AI Initiative small compute grants:** small-project applications are reviewed on a rolling basis and the initiative says calls are open to researchers in Europe and beyond. The public page does not specifically confirm a mainland-China individual applicant's eligibility or remote access to Alps. Ask the small-grants contact before preparing a proposal. The 2026 large-project deadline (September 14, 2026) has passed.
- **OpenAI Researcher Access Program:** this is API credit, not GPU training compute, and its eligibility is limited to countries supported by the OpenAI API. Do not treat mainland China as eligible without checking the current supported-country list; not a current priority for Neuron's compute needs.
- **OpenMined current grant:** the active call is specifically about ensembles, routing, and model composition, so it is not aligned with Neuron's present core research question. Revisit only if a future call fits learned compression or streaming model architecture.

### Removed from current application plan

U.S.-residency-dependent opportunities, including the Mozilla Fellowship route previously considered, are not part of the current plan. Do not use a U.S. address or claim U.S. residence. Reconsider only if the applicant independently changes their actual legal/primary residence and explicitly asks to reassess.
