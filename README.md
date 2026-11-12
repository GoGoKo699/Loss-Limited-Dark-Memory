# Loss-Limited Dark Memory

**Can a passive quantum memory retain useful capacity when collective-loss calibration is imperfect and independent noise remains?**

A common dark subspace can remove collective emission while independent local loss continues. For arbitrary supplied collective lowering profiles, this project quantifies the resulting capacity cost, gives a finite channel-uncertainty guarantee, and constructs a small memory with an explicit advantage over classical storage.

## Principal results

Let $`B`$ two-level emitters experience $`r`$ independent collective lowering profiles. Restrict storage inputs to their common kernel. All emitters count toward the rate, and encoding and decoding occur only at the boundaries of the storage interval. Independent local amplitude damping has the same excited-state survival $`\eta`$ on every emitter.

For each fixed $`1/2\lt \eta\lt 1`$, the capacity of one such cell satisfies

```math
BQ_{\mathrm{AD}}(\eta)-c_\eta r
\le Q_{\mathrm{dark}}(G,\eta)
\le BQ_{\mathrm{AD}}(\eta).
```

Here $`Q_{\mathrm{AD}}`$ is the ordinary qubit amplitude-damping capacity, and $`c_\eta`$ is an explicit constant depending only on local survival. Disjoint pair profiles incur exactly $`rQ_{\mathrm{AD}}`$ capacity loss. The worst penalty is therefore **of order $`r`$ at fixed finite local loss**, uniformly over the supplied profiles. This improves the finite overhead obtained from the ideal dark-space dimension bound.

| Result | Operational content | Scope |
|---|---|---|
| [Weighted kernel and capacity law](science/capacity.md) | At most $`c_\eta r`$ qubits of cell capacity lost relative to ordinary local damping | Dark-input architecture; homogeneous independent local loss; information-theoretic endpoint coding |
| [Robust common code](science/robustness.md) | One encoder and decoder work for a certified neighborhood of the nominal cell channel | One unknown fixed channel repeated independently across cells |
| [Efficient erasure construction](science/implementation.md) | A single-excitation dark code turns local loss into a flagged erasure | Known profile span; final-only erasure correction; polynomial endpoint algorithms |
| [Two-emitter retrieval advantage](science/operational-advantage.md) | Explicit finite margin over every classical measurement-and-record strategy | Static coupling error, independent cells, and charged storage and endpoint errors |

The mathematical step is an excitation-weighted count of the common kernel. A relative-entropy identity converts that count into coherent information at the capacity-optimal excitation population. [The proof route](science/README.md) connects those two statements.

## A finite robustness example

Encode each challenge qubit in the vacuum and nominal dark state of two emitters. Store it without intervention, then retrieve it in the basis revealed after storage. The following simultaneous budgets give a worst-case average bit-error bound of **8.15%**:

| Quantity | Budget |
|---|---:|
| Independent excitation loss | 10% |
| Relative static error in each complex collective coupling | 10% |
| Integrated additional dephasing strength per emitter | 0.01 |
| Total endpoint half-diamond error | 0.01 |

At a 10% tolerated error fraction, 2,200 independent pairs have quantum acceptance probability at least **99.11%**, while every classical strategy has acceptance probability at most **$`7.70\times10^{-10}`$**. This uses 4,400 physical emitters. The classical comparator permits a joint measurement of all inputs before storage and an unlimited classical record. The [task definition and proof](science/operational-advantage.md) state the independence, phase-reference and endpoint assumptions. The bounds are conditional on the stated certificates; their acquisition costs and confidence are [explicitly charged](science/robustness.md#4-calibration-is-paid-for). This is a theoretical guarantee, not a device measurement.

## Read the science

Start with the [scientific map](science/README.md), then follow the [physical model](science/model.md), [weighted common kernel](science/weighted-kernel.md), [capacity theorem](science/capacity.md), [uncertainty bound](science/robustness.md), [implementation costs](science/implementation.md), and [operational advantage](science/operational-advantage.md). The [prior-work comparison](science/prior-work.md) identifies inherited ingredients and the specific new conclusion. The [reference index](references/README.md) organizes the source material.

The [LLM reading guide](llms.txt) maps questions to authoritative pages.

## Learn the project

The [learning route](learning/README.md) uses Mark M. Wilde's *From Classical to Quantum Shannon Theory*, [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), as its educational anchor. The [source bridge](learning/wilde-bridge.md) connects channel capacity and entropy to the collective-loss model, weighted dark-kernel proof and explicit storage examples. The [thirty-milestone map](learning/milestones.md) progresses from local physical and information-theoretic objects to the contribution's complete operational meaning.

## Reproduce the finite checks

With Python 3.12 and the pinned numerical dependencies installed, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) explains the independent matrix calculations, the committed numerical record, and their limits. These computations check small instances and explicit channel formulas. The universal capacity theorem and asymptotic coding claims rely on the written proofs and attributed coding theorems.

## Scope and interpretation

The principal capacity theorem concerns the **dark-input restriction**, not every possible encoding into the unrestricted collective-plus-local physical channel. Fixed local loss changes the relevant benchmark: the result does not say that noise improves absolute capacity. Its constants are not uniform as local loss vanishes.

Exact darkness requires a supplied profile span and homogeneous local damping. Unknown mixing inside that span is harmless; components outside it, generic frequency disorder, nonuniform local rates, heating, and endpoint imperfections require separate error budgets. The fixed-cell compound theorem does not cover arbitrary adversarial changes between cells or correlated reservoirs. The simple pair guarantee assumes a static coupling direction during each hold interval.

The near-benchmark capacity theorem does not provide efficient near-capacity circuits. The erasure construction and pair witness give more modest guarantees with explicit endpoint resources. Finite-time boundary operations under an unbounded always-on collective reservoir are not established here; their implementation guarantee is an explicit physical input.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
