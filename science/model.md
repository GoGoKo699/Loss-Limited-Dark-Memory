# Passive storage with collective and independent loss

[Weighted kernel bound](weighted-kernel.md) · [Capacity theorem](capacity.md) · [Robustness](robustness.md) · [Operational advantage](operational-advantage.md)

The question is how much usable quantum storage is lost to collective radiation when every emitter also undergoes independent decay. We study a declared Markovian, zero-temperature model, with encoding before storage and recovery after storage. The central capacity theorem concerns encodings in the collective dark space. It does not optimize every possible encoding for the full physical channel.

## 1. One physical cell

A cell contains $`B\ge1`$ two-level emitters. Write

```math
a_j=|0\rangle\langle1|_j,\qquad
n_j=a_j^\dagger a_j,\qquad
\widehat N=\sum_{j=1}^{B}n_j.
```

The supplied collective profile matrix is $`G\in\mathbb C^{r\times B}`$, with row rank $`r`$ and $`0\le r\le B`$. Its lowering operators and common dark space are

**(M1)**

```math
L_a=\sum_{j=1}^{B}G_{aj}a_j,
\qquad
\mathcal K_G=\bigcap_{a=1}^{r}\ker L_a.
```

For $`r=0`$, the intersection is the entire physical Hilbert space. The all-ground state belongs to $`\mathcal K_G`$ for every $`G`$. Coefficients may be unequal, complex, or zero. No permutation symmetry, spatial distribution, or separation between distinct coefficients is assumed.

An invertible change of basis among the rows of $`G`$ leaves the common kernel unchanged. The relevant calibration datum for an exact dark code is therefore the supplied spatial span. Rates can be absorbed into the rows. More generally, a positive-semidefinite matrix of correlations between the supplied jumps still annihilates this common kernel. The actual dark space is exactly the supplied common kernel when that matrix is positive definite on the profile span; a singular matrix can enlarge the actual dark space. Designing for a supplied span larger than the active dissipator is therefore conservative.

Use the convention

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
```

In a rotating frame, the nominal storage generator is

**(M2)**

```math
\mathcal L
=\mathcal L_{\mathrm{col}}+\mathcal L_{\mathrm{loc}},
\qquad
\mathcal L_{\mathrm{col}}=\sum_{a=1}^{r}\mathcal D[L_a],
\qquad
\mathcal L_{\mathrm{loc}}=\kappa\sum_{j=1}^{B}\mathcal D[a_j].
```

The independent local-loss rate $`\kappa\ge0`$ is the same on every emitter. At storage time $`t`$, put

**(M3)**

```math
\eta=e^{-\kappa t}.
```

The single-emitter amplitude-damping channel $`\mathcal A_\eta`$ has Kraus operators

**(M4)**

```math
K_0=|0\rangle\langle0|+\sqrt\eta\,|1\rangle\langle1|,
\qquad
K_1=\sqrt{1-\eta}\,|0\rangle\langle1|.
```

Thus $`\eta`$ is the excited-state survival probability, not the loss probability. The local semigroup alone is $`\mathcal A_\eta^{\otimes B}`$.

The ideal model permits arbitrarily large finite collective rates. It assumes an initially unexcited environment for the lowering dissipators and uses their stated Lindblad description. The exact microscopic vacuum invariance in the earlier [Multimode Dark Memory model](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/model.md) is a separate result. We do not replace arbitrary non-Markovian local reservoirs by (M2) without justification.

## 2. Local loss preserves the whole dark space

**Lemma 1 — Grading.** The common dark space is an orthogonal direct sum of excitation sectors:

**(M5)**

```math
\mathcal K_G
=\bigoplus_{k=0}^{B}\mathcal K_{G,k},
\qquad
\mathcal K_{G,k}
=\mathcal K_G\cap\ker(\widehat N-kI).
```

In particular its orthogonal projector $`P_G`$ commutes with $`\widehat N`$.

**Proof.** Every $`L_a`$ lowers excitation by one. If $`\psi=\sum_k\psi_k`$ is its excitation decomposition, the vectors $`L_a\psi_k`$ lie in distinct excitation sectors. They cannot cancel. Therefore $`L_a\psi=0`$ for every $`a`$ if and only if each $`\psi_k`$ belongs to the common kernel. $`\square`$

**Lemma 2 — Invariance under independent loss.** For every $`0\le\eta\le1`$, the channel $`\mathcal A_\eta^{\otimes B}`$ maps operators supported on $`\mathcal K_G`$ to operators supported on the same space. The assertion remains true with an arbitrary untouched reference system.

**Proof.** Operators $`a_j`$ commute with one another, including at the same site, and hence

```math
[a_j,L_a]=0
```

for all indices. Consequently every product $`a_S=\prod_{j\in S}a_j`$ preserves the common kernel. Lemma 1 shows that every function of $`\widehat N`$ also preserves it.

For $`0\lt \eta\lt 1`$, a product Kraus operator of the independent amplitude-damping channel, indexed by the set $`S`$ of emitters that lose an excitation, can be written

**(M6)**

```math
K_S
=\left(\frac{1-\eta}{\eta}\right)^{|S|/2}
a_S\eta^{\widehat N/2}.
```

Both factors preserve $`\mathcal K_G`$. Therefore every Kraus branch maps the space into itself. The cases $`\eta=0,1`$ follow directly or by continuity. Tensoring the argument with a reference identity does not change it. $`\square`$

**Proposition 3 — Exact reduction of simultaneous loss.** For every operator $`\rho`$ supported on $`\mathcal K_G`$,

**(M7)**

```math
e^{t\mathcal L}(\rho)
=\mathcal A_{e^{-\kappa t}}^{\otimes B}(\rho).
```

This is an equality of channels on the entire dark input space, including reference-entangled inputs.

**Proof.** Every collective dissipative term vanishes on an operator supported on $`\mathcal K_G`$: $`L_a\rho=0`$, $`\rho L_a^\dagger=0`$, and both anticommutator terms vanish. By Lemma 2, the candidate trajectory

```math
\rho(t)=\mathcal A_{e^{-\kappa t}}^{\otimes B}(\rho)
```

stays supported on $`\mathcal K_G`$. At every time it therefore satisfies

```math
\frac{d\rho(t)}{dt}
=\mathcal L_{\mathrm{loc}}(\rho(t))
=\mathcal L(\rho(t)).
```

Uniqueness of the finite-dimensional master-equation solution proves (M7). $`\square`$

The proof does **not** require $`\mathcal L_{\mathrm{col}}`$ and $`\mathcal L_{\mathrm{loc}}`$ to commute on the full operator space. Nor does it say that the logical information is unaffected by local loss. Local loss changes the stored state, but it does so entirely within a space on which the collective dissipator remains inactive. Terminal error correction addresses that remaining loss.

The same argument allows time-dependent positive collective rates or mixing within the supplied span. It also allows a known time-dependent common local rate, with $`\eta=\exp[-\int_0^t\kappa(s)\,ds]`$. These extensions retain homogeneous local damping.

## 3. Hamiltonian conventions

A common emitter Hamiltonian $`H_A=\omega\widehat N`$ preserves $`\mathcal K_G`$. It adds a known excitation-dependent phase to (M7), removable by one terminal unitary. We work in the corresponding rotating frame. This convention requires a known phase reference or an explicitly budgeted phase error; it does not protect an unknown relative phase between different excitation sectors.

Terms of the form

```math
H_{\mathrm{dark}}(s)
=\sum_{a,b}h_{ab}(s)L_a^\dagger L_b,
\qquad h(s)=h(s)^\dagger,
```

annihilate the common kernel. They remain inactive along the local-loss trajectory in Proposition 3. General frequency disorder, exchange Hamiltonians, or nonuniform independent-loss rates need not preserve the kernel and require the separate [robustness analysis](robustness.md).

## 4. Capacity of the dark-input architecture

Choose any isometry $`V_G:\mathbb C^{d_G}\to(\mathbb C^2)^{\otimes B}`$ onto $`\mathcal K_G`$, where $`d_G=\dim\mathcal K_G`$. Define the effective cell channel

**(M8)**

```math
\mathcal N_{G,\eta}(\rho)
=\mathcal A_\eta^{\otimes B}(V_G\rho V_G^\dagger),
\qquad
Q_{\mathrm{dark}}(G,\eta)=Q(\mathcal N_{G,\eta}).
```

The choice of basis isometry changes no capacity. The output is the complete $`B`$-emitter register; recovery may use all of it.

Here $`Q`$ is the usual unassisted quantum capacity, measured in logical qubits per use of this cell. For $`m`$ independently repeated cells, an encoder transfers an unknown payload into $`\mathcal K_G^{\otimes m}`$, all cells undergo their storage channels, and one final decoder recovers the payload. Reliability means entanglement fidelity tending to one as $`m\to\infty`$. Input states may be entangled across cells and with an inaccessible reference.

Every quantum carrier present during storage belongs to the $`mB`$ physical emitters. No additional protected quantum register, retained original payload, entanglement-assistance supply, or intermediate quantum communication is part of this interface. Code descriptions and independent classical randomness are permitted. There is no measurement, feedback, reset, dynamical decoupling, or fresh quantum ancilla during storage.

The asymptotic rate per physical emitter is $`Q_{\mathrm{dark}}(G,\eta)/B`$. Its definition first takes the ordinary coding limit in the number of cells. A subsequent statement as $`B/r\to\infty`$ concerns these capacities, or a justified diagonal choice of sufficiently long codes. It does not by itself prove that one growing cell stores an arbitrary payload with vanishing error.

The restriction in (M8) is material. Proposition 3 identifies the channel on dark inputs, but makes no claim about unrestricted encodings into bright sectors. Accordingly, an upper bound on $`Q_{\mathrm{dark}}`$ is not an upper bound on the capacity of the complete physical dissipative channel.

## 5. Resources and imperfections

| Resource or assumption | Treatment |
| --- | --- |
| Physical storage width | All $`B`$ emitters per cell, including initialized redundancy, are counted. |
| Encoding and recovery | Boundary operations are allowed. Capacity existence is distinct from an efficient circuit construction. |
| Collective profile | A nominal finite classical description determines the code. Calibration error changes the storage channel and is treated separately. |
| Local loss | A nonzero independent loss floor is included exactly through $`\eta`$. |
| Additional noise | Fixed-cell channel uncertainty is bounded in [Robustness](robustness.md); generic noise is not silently included in (M7). |
| Classical baseline and task | A concrete retrieval task is stated in [Operational advantage](operational-advantage.md). Storage capacity alone is not a computational speedup claim. |

In the exact model, collective strength does not enter the dark-input capacity. A tolerance for an error in a strong collective jump can nevertheless depend on that strength. Uniform exact protection and uniform robustness are different assertions.

The common-kernel criterion and vacuum dark-memory interpretation are established decoherence-free-subspace tools. The earlier [Multimode Dark Memory account](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/rank-law.md) supplies the unweighted dimension argument used below. Our [weighted refinement](weighted-kernel.md) connects that algebra to the local-loss capacity benchmark; [Prior work](prior-work.md) gives the detailed comparison.
