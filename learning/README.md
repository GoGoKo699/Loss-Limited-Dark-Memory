# Learning route

The scientific question is whether passive protection against collective emission remains useful once independent loss, uncertain calibration and endpoint costs are counted. This route connects the physical mechanism to the capacity proof and then to an explicit storage task.

## One source, connected to the project

The educational anchor is **Mark M. Wilde, *From Classical to Quantum Shannon Theory*, [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8)**, posted 14 July 2019. This is the author's draft associated with *Quantum Information Theory*, second edition (Cambridge University Press, 2017).

Start with the [Wilde-to-project bridge](wilde-bridge.md). It selects the relevant parts of the source, translates notation, and supplies the missing collective-loss and dark-kernel steps. The anchor supports the foundations; the primary research dependencies and new derivations remain identified in the [scientific account](../science/README.md) and [references](../references/README.md).

## Thirty understanding targets

The [milestone map](milestones.md) contains exactly thirty project-defined targets in two phases:

| Phase | Milestones | Direction of the story |
|---|---|---|
| Background and preliminaries | M01–M12 | From one noisy qubit and a protected state to coherent information, capacity and a fair storage task |
| Narrative and innovation | M13–M30 | From dark-space invariance and the weighted count to the sharp rank penalty, quantified uncertainty, explicit constructions and the complete operational comparison |

Each milestone states its central question, understanding target, dependencies, conceptual connection and source pointers. The map describes the scientific connections needed to understand the result; technical details remain in their authoritative proof pages.

## Choose a reading route

| Reader's question | Route |
|---|---|
| What does the memory actually do? | [Bridge and worked cell](wilde-bridge.md), then [physical model](../science/model.md) and [two-emitter retrieval](../science/operational-advantage.md) |
| Why is the finite penalty proportional to collective rank? | [Weighted kernel](../science/weighted-kernel.md), then [capacity theorem](../science/capacity.md) |
| Which imperfections are tolerated? | [Robustness and paid calibration](../science/robustness.md), then [implementation assumptions](../science/implementation.md) |
| Which rates have explicit efficient endpoints? | [Single-excitation erasure construction](../science/implementation.md), compared with the [general capacity guarantee](../science/capacity.md) |
| How can the finite formulas be checked? | [Verification guide](../verification/README.md) and its committed numerical record |

The three performance statements serve different purposes: the general theorem bounds dark-input capacity, the erasure construction gives a lower rate with polynomial endpoint algorithms under its exact model, and the pair task supplies a finite robustness witness. Keep their assumptions and resources attached when moving between them.
