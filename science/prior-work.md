# Prior work and the contribution

The question here is how much quantum communication rate is lost when an emitter memory must avoid collective loss in a supplied profile span while also undergoing independent local loss. Dark subspaces, amplitude-damping capacity, concatenated protection, and channel-uncertainty coding are established ingredients. The result developed in this repository concerns their particular combination: a uniform, finite capacity penalty controlled by the number of supplied collective lowering profiles.

The [model](model.md) defines $`B`$ emitters, $`r`$ linearly independent profiles, their common kernel $`K_G`$, and homogeneous independent amplitude damping with survival probability $`\eta`$. For fixed $`1/2<\eta<1`$, the [capacity account](capacity.md) proves

```math
B Q_{\mathrm{AD}}(\eta)-c_\eta r
\;\leq\;
Q_{\mathrm{dark}}(G,\eta)
\;\leq\;
B Q_{\mathrm{AD}}(\eta).
```

Here $`Q_{\mathrm{dark}}`$ is the capacity with inputs restricted to $`K_G`$. The upper bound is not a converse for every possible encoding into the full simultaneous collective-plus-local-loss channel. The [weighted-kernel argument](weighted-kernel.md) supplies the input state needed for the lower bound. The matched worst-profile penalty is of order $`r`$ at fixed finite loss.

## 1. What is inherited

### Dark storage under collective amplitude damping

Duan and Guo established optimal dark encodings for homogeneous collective amplitude damping. Their one-mode kernel has dimension $`\binom{B}{\lfloor B/2\rfloor}`$, giving an asymptotic logical rate of one. This is an important direct antecedent: a large radiative dark space and its use for quantum storage are not new here. Their model does not supply the present finite independent-loss capacity comparison. [R1]

The public *Multimode-Dark-Memory* account extends the ideal-storage dimension question to arbitrary supplied inhomogeneous profiles. At the pinned revision below, it proves a common-kernel dimension bound by a commuting-nilpotent injection, develops the worst-profile ideal redundancy of order $`r\log(B/r)`$, and separates code existence from compiler and precision costs. Its exact model explicitly excludes independent emission from the protected interaction class. [R2]

This repository inherits that common-kernel model and injection. The new algebraic step keeps the excitation grading rather than counting every vector equally:

```math
Z_{K_G}(z)
=\operatorname{Tr}(P_{K_G}z^{\widehat N})
\;\geq\;
(1+z)^B(1-z)^r,
\qquad 0<z<1.
```

The earlier dimension bound can already be combined with an amplitude-damping thinning argument to achieve the asymptotic independent-loss benchmark when $`r=o(B)`$. That route bounds the capacity deficit by $`B-\log_2\dim K_G`$. Consequently, asymptotic benchmark matching alone does not require the weighted refinement. The refinement improves the finite penalty to $`O_\eta(r)`$ and yields the matched noisy rank law. It controls the weight of the capacity-optimal Bernoulli product input in the dark space; that input is not generally maximally mixed.

### Combining passive protection and error correction

Lidar, Bacon and Whaley combined decoherence-free subspaces with quantum error-correcting codes to protect against symmetry-breaking perturbations, including independent decoherence. Their work already establishes the general idea of using passive protection against a dominant collective channel and error correction against residual noise. [R3]

Accordingly, this project does not claim that adding an outer code to a dark memory is itself a new mechanism. The additional assertion is quantitative: at fixed homogeneous local loss, arbitrary supplied rank-$`r`$ lowering profiles cost at most $`c_\eta r`$ bits of cell capacity relative to the ordinary independent-loss benchmark. The finite-error extension uses imported continuity and compound-coding results; it does not replace them.

### Physically related waveguide and constant-excitation constructions

Paulisch, Kimble and González-Tudela studied computation in waveguide-QED decoherence-free subspaces, including unguided decay and imperfect controls. That work provides a close physical precedent for a collective radiative channel accompanied by independent loss. Its central results concern protected encodings and gate implementation rather than a uniform arbitrary-profile capacity penalty. [R4]

Ouyang's rotated concatenated codes combine constant-excitation protection against coherent collective phase errors with stabilizer-code correction. This is a useful comparison for endpoint encodings and residual amplitude-damping errors, but its protected collective operator and rate question differ from the common lowering kernel used here. [R5]

## 2. The capacity benchmark is established

For the qubit amplitude-damping channel with excited-state survival $`\eta`$, the established unassisted quantum capacity is

```math
Q_{\mathrm{AD}}(\eta)
=
\begin{cases}
\displaystyle\max_{0\leq p\leq1}
\left[h_2(\eta p)-h_2((1-\eta)p)\right],
& \eta\geq \tfrac12,\\[4pt]
0,& \eta\leq\tfrac12.
\end{cases}
```

Giovannetti and Fazio derived this benchmark in their information-capacity treatment of spin-chain channels. Wolf and Pérez-García placed amplitude damping within the capacity classification of qubit channels with a two-dimensional environment. Degradability and the resulting single-letter expression are imported facts. [R6, R7]

The new comparison concerns a restriction of the input alphabet of a product amplitude-damping channel. Homogeneous independent loss preserves $`K_G`$: each local lowering operator commutes with every collective lowering operator, and the uniform no-jump evolution depends only on $`\widehat N`$. Collective loss therefore remains inactive throughout the local-loss evolution of a dark input.

The weighted dark Gibbs state has a relative-entropy cost of at most $`c_\eta r`$ compared with the capacity-optimal Bernoulli product input. Expanding coherent information around that product input makes the mean-excitation term vanish at the optimal population. Data processing then converts the weighted-kernel bound into the finite capacity penalty. The entropy identities and data-processing inequality are standard; the particular dark-input bound and its noisy rank consequence are the contribution.

The comparison with ideal storage has a precise scope. At $`\eta=1`$, worst-profile dark redundancy is of order $`r\log(B/r)`$ in the sublinear-rank regime. At each fixed $`1/2<\eta<1`$, the penalty relative to the corresponding local-loss benchmark is of order $`r`$. The benchmarks differ, $`c_\eta`$ diverges as $`\eta`$ approaches one, and this does not assert that adding noise increases absolute capacity.

## 3. Correlated-damping capacity papers use different channels

D'Arrigo and collaborators compute capacities of a two-qubit fully correlated amplitude-damping channel. Its correlated branch allows a simultaneous two-excitation decay while leaving the other three basis states noiseless; the partially correlated model is a mixture of this branch and independent damping. This is different from a collective one-excitation jump $`\sum_jg_j\sigma_j^-`$ acting simultaneously with local loss. [R8]

Jahangir, Arshed and Toor analyze an amplitude-damping channel with memory built from correlated and uncorrelated branches. Their correlated Lindblad jump is proportional to $`\sigma^-\otimes\sigma^-`$, again distinct from the sum of one-site lowerings. Their capacity results therefore do not establish the present arbitrary-profile dark-input rank law. [R9]

These distinctions concern the actual generators and operational channel models, rather than the shared phrase “correlated amplitude damping.”

## 4. A recent finite-code comparator

Chandra, Ouyang, Muraleedharan and Brennen develop recovery for permutation-invariant codes, including CAD codes adapted to collective amplitude damping. Their full text studies the uniform collective $`J_-`$ channel and homogeneous independent damping, constructs finite code families, and compiles noisy recovery circuits. Sections III.B–C and V–VI were inspected. [R10]

This is a relevant endpoint-recovery comparison: applying recovery after storage is compatible with the passive interval allowed here. Its code constructions and fidelity benchmarks do not supply the weighted common-kernel capacity bound for arbitrary inhomogeneous profiles or the matched noisy rank law.

## 5. Robustness ingredients and the finite witness

The uncertainty extension distinguishes one unknown fixed cell channel, repeated independently, from arbitrary correlations between damaged cells. Bjelaković, Boche and Nötzel supply the compound-channel coding theorem needed for one common encoder and decoder. Winter's conditional-entropy continuity bound supplies the fixed-input coherent-information penalty. These are applications of established theorems, not new universal-coding or continuity results. [R11, R12]

The two-emitter example provides a small operational witness of useful storage with static coupling error and additional noise. Subradiance, a vacuum-plus-dark-state encoding, and quantum-memory advantages in delayed-measurement tasks are established ideas; the [operational account](operational-advantage.md) specifies the task and attributes its classical benchmark. The purpose of the example is to make the physical assumptions, endpoint resources, and finite error margin explicit. It is not the source of the rank-capacity claim.

Several distinctions remain load bearing:

- Unknown mixing within a supplied profile span preserves exact darkness. A component outside that span is a perturbation and must be budgeted.
- A fixed misaligned bright direction in the pair example is different from arbitrary time-dependent changes of that direction.
- Collective Lamb terms built from $`L_a^\dagger L_b`$ vanish on the exact dark space. General frequency disorder need not.
- The generic finite-cell perturbation radius can depend on collective coupling strength. The special static pair bound has stronger storage-interval behavior.
- Counting endpoint gates does not establish fast, accurate implementation under an unbounded always-on reservoir. Endpoint errors must be included when applying the physical budget.

## 6. Literature-review boundary

The comparison was updated on 12 November 2026. The main primary papers above were accessed in full text for their relevant models and results; the pinned public antecedent was read at the specified revision. Searches targeted collective damping with independent loss, common-kernel capacity, weighted dark partition functions, and rank-dependent capacity deficits. No exact antecedent for the weighted $`O_\eta(r)`$ capacity deficit or its matching noisy rank law was located in that bounded review.

This is a statement about the inspected literature, not a certification that no antecedent exists. In particular, an abstract-level match, a shared noise label, or a result for a different channel does not decide priority. The contribution is stated narrowly enough to permit direct comparison with any subsequently identified source.

## References

**R1.** L.-M. Duan and G.-C. Guo, “Optimal quantum codes for preventing collective amplitude damping,” *Physical Review A* **58**, 3491 (1998). [Primary preprint](https://arxiv.org/abs/quant-ph/9804014) · [Publisher](https://doi.org/10.1103/PhysRevA.58.3491).

**R2.** *Multimode-Dark-Memory*, public scientific repository, revision f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb. [Pinned model](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/model.md) · [Pinned rank law and injection proof](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/rank-law.md) · [Pinned encoding and precision account](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/encoding-and-precision.md).

**R3.** D. A. Lidar, D. Bacon and K. B. Whaley, “Concatenating Decoherence Free Subspaces with Quantum Error Correcting Codes,” *Physical Review Letters* **82**, 4556 (1999). [Primary preprint](https://arxiv.org/abs/quant-ph/9809081) · [Publisher](https://doi.org/10.1103/PhysRevLett.82.4556).

**R4.** V. Paulisch, H. J. Kimble and A. González-Tudela, “Universal quantum computation in waveguide QED using decoherence free subspaces,” *New Journal of Physics* **18**, 043041 (2016). [Primary preprint](https://arxiv.org/abs/1512.04803) · [Publisher](https://doi.org/10.1088/1367-2630/18/4/043041).

**R5.** Y. Ouyang, “Avoiding coherent errors with rotated concatenated stabilizer codes,” *npj Quantum Information* **7**, 87 (2021). [Primary preprint](https://arxiv.org/abs/2010.00538) · [Publisher](https://doi.org/10.1038/s41534-021-00429-8).

**R6.** V. Giovannetti and R. Fazio, “Information-capacity description of spin-chain correlations,” *Physical Review A* **71**, 032314 (2005). [Primary preprint, version 3](https://arxiv.org/abs/quant-ph/0405110v3) · [Publisher](https://doi.org/10.1103/PhysRevA.71.032314).

**R7.** M. M. Wolf and D. Pérez-García, “Quantum Capacities of Channels with Small Environment,” *Physical Review A* **75**, 012303 (2007). [Primary preprint](https://arxiv.org/abs/quant-ph/0607070) · [Publisher](https://doi.org/10.1103/PhysRevA.75.012303).

**R8.** A. D'Arrigo, G. Benenti, G. Falci and C. Macchiavello, “Classical and quantum capacities of a fully correlated amplitude damping channel,” *Physical Review A* **88**, 042337 (2013). [Primary full text, version 3](https://arxiv.org/html/1309.2219v3) · [Publisher](https://doi.org/10.1103/PhysRevA.88.042337).

**R9.** R. Jahangir, N. Arshed and A. H. Toor, “Quantum capacity of an amplitude-damping channel with memory,” *Quantum Information Processing* **14**, 765 (2015). [Primary full text, version 3](https://arxiv.org/html/1207.5612v3) · [Publisher](https://doi.org/10.1007/s11128-014-0883-y).

**R10.** O. Chandra, Y. Ouyang, G. Muraleedharan and G. K. Brennen, “Recovery Algorithm for Correlated Errors in Permutation-Invariant Quantum Codes,” arXiv:2607.02346v1 (2026). [Primary record](https://arxiv.org/abs/2607.02346v1) · [Full HTML](https://arxiv.org/html/2607.02346v1) · [Full PDF](https://arxiv.org/pdf/2607.02346).

**R11.** I. Bjelaković, H. Boche and J. Nötzel, “Entanglement transmission and generation under channel uncertainty: Universal quantum channel coding,” *Communications in Mathematical Physics* (2009). [Primary preprint, version 3](https://arxiv.org/abs/0811.4588v3) · [Publisher](https://doi.org/10.1007/s00220-009-0887-0).

**R12.** A. Winter, “Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints,” *Communications in Mathematical Physics* **347**, 291–313 (2016). [Primary preprint, version 6](https://arxiv.org/abs/1507.07775v6) · [Publisher](https://doi.org/10.1007/s00220-016-2609-8).
