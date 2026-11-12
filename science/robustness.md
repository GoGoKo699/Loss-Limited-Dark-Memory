# Calibration uncertainty and additional noise

[Storage model](model.md) · [Capacity theorem](capacity.md) · [Operational advantage](operational-advantage.md) · [Implementation](implementation.md)

The exact dark-space reduction survives arbitrary uncertainty in the coefficients of collective modes whose spatial span is supplied. Errors in the supplied spatial span itself require a quantitative tolerance. This page gives a common-code guarantee for a finite cell, sufficient channel-error certificates, and explicit costs for acquiring the required calibration information. The two-emitter calculation in [Operational advantage](operational-advantage.md) gives a stronger, strength-independent tolerance for a particular task.

## 1. What must be stable

Fix a cell size $`B`$, a nominal profile matrix $`G`$ of row rank $`r`$, a storage time $`t`$, and $`1/2\lt \eta=e^{-\kappa t}\lt 1`$. Let $`V_G`$ embed an abstract input space of dimension $`d_G=\dim\mathcal K_G`$ into the nominal common dark space. The ideal cell channel is

**(R1)**

```math
\mathcal N_0(\rho)
=\mathcal A_\eta^{\otimes B}(V_G\rho V_G^\dagger).
```

The actual channel belongs to a declared set $`\mathfrak I`$ of channels with this same input and output interface. We assume

**(R2)**

```math
\sup_{\mathcal N\in\mathfrak I}
\frac12\|\mathcal N-\mathcal N_0\|_\diamond\le\epsilon,
\qquad 0\le\epsilon\le1.
```

The diamond norm includes an arbitrary reference entangled with the input. It is sufficient to certify (R2) on the nominal encoded input space; the physical channel can behave very differently on unused bright inputs.

For the common-code theorem, one unknown $`\mathcal N\in\mathfrak I`$ is fixed and the $`m`$ storage cells undergo $`\mathcal N^{\otimes m}`$. The encoder and decoder know the set, but need not know the realized channel. A shared static classical parameter is allowed: a code that works uniformly for every parameter also works after averaging over that parameter. A dynamical environment coupling different cells, or arbitrary cell-by-cell switching among channels, is a different model. The elementary pair task and the erasure construction below have their own, less restrictive statements for independent nonidentical cells.

No control is applied during the storage interval. Calibration is performed on separate systems before payload storage. Boundary encoding and recovery are allowed, with their implementation assumptions stated in [Implementation](implementation.md).

## 2. One encoder and one decoder for the whole uncertainty set

Write

**(R3)**

```math
g(\epsilon)=(1+\epsilon)
h_2\!\left(\frac{\epsilon}{1+\epsilon}\right).
```

The constants $`Q_{\mathrm{AD}}(\eta)`$ and $`c_\eta`$ are defined in [the capacity theorem](capacity.md).

**Theorem 1 — Robust finite-cell rate.** Under (R2) and the fixed-channel product-use assumption, every strictly smaller nonnegative rate than

**(R4)**

```math
R_{\mathrm{rob}}
=Q_{\mathrm{AD}}(\eta)
-\frac{c_\eta r}{B}
-\frac{2\epsilon\log_2 d_G+g(\epsilon)}{B}
```

is achievable in logical qubits per physical emitter by a sequence of common encoders and decoders whose entanglement fidelity tends to one uniformly over $`\mathfrak I`$. In particular the simpler lower bound is

**(R5)**

```math
R_{\mathrm{rob}}
\ge Q_{\mathrm{AD}}(\eta)
-\frac{c_\eta r}{B}
-2\epsilon-\frac{g(\epsilon)}{B}.
```

A negative right-hand side gives no positive-rate certificate. The physical width is $`mB`$, including every initialized redundant emitter.

**Proof.** Use the same nominal dark Gibbs state $`\rho_*`$ for every channel in the set. The weighted-kernel argument proves

```math
I_c(\rho_*,\mathcal N_0)
\ge BQ_{\mathrm{AD}}(\eta)-c_\eta r.
```

Purify $`\rho_*`$ with a reference $`R`$ of dimension at most $`d_G`$. Condition (R2) bounds the trace distance of the two reference-output states by $`\epsilon`$. Coherent information equals minus their conditional entropy $`S(R\mid Y)`$. Winter's conditional-entropy continuity bound, Lemma 2 of [the primary paper](https://arxiv.org/pdf/1507.07775), gives

**(R6)**

```math
I_c(\rho_*,\mathcal N)
\ge I_c(\rho_*,\mathcal N_0)
-2\epsilon\log_2d_G-g(\epsilon)
\quad\text{for every }\mathcal N\in\mathfrak I.
```

The uninformed-encoder, uninformed-decoder compound-channel theorem of Bjelaković, Boche, and Nötzel, Theorem 1 of [the primary paper](https://arxiv.org/pdf/0811.4588), states

**(R7)**

```math
Q(\mathfrak I)
=\lim_{\ell\to\infty}\frac1\ell
\max_{\rho_\ell}\inf_{\mathcal N\in\mathfrak I}
I_c(\rho_\ell,\mathcal N^{\otimes\ell}).
```

Taking product copies of the fixed $`\rho_*`$ in (R7) yields
$`Q(\mathfrak I)\ge\inf_{\mathcal N\in\mathfrak I}I_c(\rho_*,\mathcal N)`$.
Combine this with (R6), divide by $`B`$, and use $`\log_2d_G\le B`$. $`\square`$

This argument produces one common code. Continuity of each separately optimized channel capacity would not, by itself, produce a decoder independent of the unknown calibration. The compound theorem is an existence theorem; it does not establish efficient circuits near the rate (R4).

For a fixed finite cell with a strict positive nominal margin, continuity leaves a nonzero admissible error interval. Its width need not shrink with the number $`m`$ of cells. It can depend on $`B,r,t`$ and on the physical calibration certificate. The large-cell limit in the ideal capacity theorem does not automatically allow a fixed microscopic error per emitter in a single growing cell.

## 3. Sufficient physical error certificates

### 3.1 A direct generator estimate

Use $`\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2`$. Suppose the nominal and actual finite-dimensional generators are

**(R8)**

```math
\begin{aligned}
\mathcal L_0&=\sum_a\mathcal D[L_a]+\mathcal L_{\mathrm{loc}},\\
\mathcal L_1&=\sum_a\mathcal D[L_a+E_a]
 +\mathcal L_{\mathrm{loc}}-i[\Delta H,\cdot]+\mathcal R,
\end{aligned}
```

and both generate completely positive trace-preserving evolution. The extra term $`\mathcal R`$ can include added local noise or a change in the local-loss generator. Rates are included in the jump amplitudes. Operator norms below are spectral norms; generator norms are diamond norms.

**Proposition 2.** A sufficient error radius is

**(R9)**

```math
\epsilon_{\mathrm{hold}}
\le\min\!\left\{1,\,
t\sum_a\bigl(2\|L_a\|\|E_a\|+\|E_a\|^2\bigr)
 +t\|\Delta H\|
 +\frac t2\|\mathcal R\|_\diamond\right\}.
```

**Proof.** Expanding the jump dissipators and using
$`\|X(\cdot)Y\|_\diamond\le\|X\|\|Y\|`$ gives

```math
\|\mathcal D[L+E]-\mathcal D[L]\|_\diamond
\le4\|L\|\|E\|+2\|E\|^2,
\qquad
\|[\Delta H,\cdot]\|_\diamond\le2\|\Delta H\|.
```

Duhamel's formula reads

```math
e^{t\mathcal L_1}-e^{t\mathcal L_0}
=\int_0^t e^{(t-s)\mathcal L_1}
(\mathcal L_1-\mathcal L_0)e^{s\mathcal L_0}\,ds.
```

Every channel on either side of the generator difference has diamond norm one. Taking the half-diamond norm proves (R9), including on any encoded input subspace. $`\square`$

For time-dependent generators, replace each $`t`$ times a norm by its time integral, using the corresponding propagators. This estimate does not assume that the collective and added generators commute. A dephasing process that transfers a dark state into a bright sector is therefore included.

Large nominal collective strengths can make the general bound (R9) restrictive. Exact darkness under strong collective loss is not itself a strength-independent calibration theorem. The fixed pair calculation provides such a theorem for its declared static direction error.

### 3.2 Uncertainty that leaves the supplied span unchanged

Suppose the actual collective jumps have the form

**(R10)**

```math
\widetilde L_a(s)=\sum_b M_{ab}(s)L_b,
```

with arbitrary unknown coefficients, strengths, and time dependence. Every $`\widetilde L_a(s)`$ still annihilates $`\mathcal K_G`$. The local-loss invariance proof then makes their dissipators exactly inactive throughout storage. The same is true of any Hermitian Hamiltonian $`\sum_{a,b}h_{ab}(s)L_a^\dagger L_b`$. No accuracy requirement is imposed on these coefficients. A supplied span may conservatively contain modes that are absent in the actual sample.

The spatial span itself is a resource. Manufacturing information or a calibration procedure must supply it; unknown directions outside it are not covered by (R10). Uniform local damping, the zero-temperature lowering model, and the absence of unwanted Hamiltonian action within the code remain assumptions.

### 3.3 Conditioning when a kernel is inferred

A small matrix-entry error does not imply a uniformly small change in a kernel at a rank-changing point. This is visible already in the one-excitation sector, where the dark subspace is $`\ker G`$.

For an estimate $`\widehat G`$ of the same row rank as $`G`$, suppose

```math
\|G-\widehat G\|\le\xi,
\qquad s=\sigma_{\min}^{+}(\widehat G)>\xi.
```

For a unit vector $`v\in\ker\widehat G`$,

**(R11)**

```math
\mathrm{dist}(v,\ker G)
\le\frac{\|Gv\|}{\sigma_{\min}^{+}(G)}
\le\frac{\xi}{s-\xi}.
```

Here the first inequality follows by resolving $`v`$ into the kernel and its orthogonal complement; the second uses the singular-value perturbation bound. With equal kernel dimensions this also bounds the largest principal-angle sine. Thus a reliable inferred subspace requires a gap as well as an entry-error estimate.

For the entire many-excitation dark space, the corresponding map is the stacked lowering map $`\psi\mapsto(L_1\psi,\ldots,L_r\psi)`$. The same argument applies only with its own positive singular-value gap and a stable kernel dimension. A gap for the small profile matrix alone is not a gap certificate for this larger map.

A direct channel certificate such as (R2) avoids reconstructing an ill-conditioned microscopic profile. The pair geometry in [Operational advantage](operational-advantage.md) is an explicit, well-conditioned exception with a sharp $`\delta^2`$ leakage bound.

## 4. Calibration is paid for

The following protocols distinguish the channel promise used in a theorem from the observations used to support it. Their confidence statements require independent repetitions and stationarity across calibration and deployment, or a separate bound on subsequent drift. They do not infer those assumptions from the same finite data.

### 4.1 Direct certification of the retrieval task

For the pair task, run $`N_{\mathrm{cal}}`$ independent fresh BB84 challenges through the complete preparation, hold, retrieval, and basis-measurement procedure. Let $`\widehat p`$ be the observed bit-error fraction. Hoeffding's bound gives the one-sided certificate

**(R12)**

```math
p\le\widehat p+
\left(\frac{\ln(1/\beta)}{2N_{\mathrm{cal}}}\right)^{1/2}
\quad\text{with probability at least }1-\beta.
```

For example, $`N_{\mathrm{cal}}=23026`$ certifies a $`0.01`$ additive margin at confidence $`0.99`$. Each trial consumes a fresh challenge, two emitter uses for duration $`t`$, constant-size endpoint operations, and one final bit measurement. Reusing a physical pair requires reset and independently renewed reservoirs between trials. Parallel calibration uses the corresponding additional physical width.

This certifies the task's average error under the tested challenge distribution. It does not certify a diamond-norm radius, characterize every input, or prove a microscopic coupling bound. Trusted state preparation and a trusted basis/bit label are part of this test. Detector imperfections may be included in the score if the objective is the actual end-to-end task.

For a heterogeneous array, testing one pair alone does not certify the other pairs. There is nevertheless a direct average-error protocol: on each calibration trial select a physical pair uniformly with replacement, reset it, and run a fresh independent challenge. Under pairwise stationarity and independent resets, the error indicators are independent Bernoulli variables of mean $`\overline p=m^{-1}\sum_i p_i`$, so (R12) certifies $`\overline p`$ with the same sample count. At deployment, the independent-pair concentration bound in [Operational advantage](operational-advantage.md) needs only this mean bound. This protocol includes every selected pair's actual endpoint procedure; arbitrary later drift or correlated deployment faults are not certified.

### 4.2 A conservative complete finite-cell calibration protocol

An explicit process-tomography construction shows that (R2) can be acquired at a finite cost for fixed $`B`$. Its exponential dependence on $`B`$ is stated rather than hidden.

Put $`D=2^B`$. Use the $`D^2`$ Hermitian Pauli strings $`P,Q`$ and define the physical channel's transfer coefficients

**(R13)**

```math
T_{QP}=D^{-1}\mathrm{Tr}[Q\mathcal T(P)].
```

For $`P\ne I`$, prepare $`\rho_{P,\pm}=(I\pm P)/D`$ and measure $`Q`$ at the output. Each mixed input can be prepared by classically sampling product Pauli eigenstates with the specified parity. The half-difference of the two output means is $`T_{QP}`$. For $`P=I`$, prepare $`I/D`$. Measuring a Pauli string uses local Pauli measurements and their classical parity; no entangled probe is required.

There are at most $`2D^4`$ preparation/measurement settings. Taking at least

**(R14)**

```math
n_0=\left\lceil\frac{2}{u^2}
\ln\frac{4D^4}{\beta}\right\rceil
```

independent samples per setting ensures that every estimated transfer entry has error at most $`u`$, simultaneously with confidence at least $`1-\beta`$.

For the normalized Choi state,

```math
J(\mathcal T)=D^{-2}\sum_{P,Q}T_{QP}P^T\otimes Q.
```

Pauli orthogonality gives $`\|\widehat J-J\|_2\le Du`$, where $`\|\cdot\|_2`$ is the Hilbert–Schmidt norm. Project the estimate to the convex set of trace-preserving completely positive Choi matrices by least squares. A conservative triangle bound gives
$`\|J_{\mathrm{fit}}-J\|_2\le2Du`$.
The trace-norm/rank inequality and the standard normalized-Choi bound
$`\|\mathcal T_1-\mathcal T_2\|_\diamond\le D\|J_1-J_2\|_1`$
then yield

**(R15)**

```math
\frac12\|\mathcal T_{\mathrm{fit}}-\mathcal T\|_\diamond
\le D^3u.
```

The Choi bound also follows directly by writing an arbitrary purified channel input as a linear map applied to one half of a normalized maximally entangled state, whose squared map norm is at most $`D`$.

Choose $`u=\epsilon_{\mathrm{cal}}/D^3`$. This sufficient protocol uses

**(R16)**

```math
N_{\mathrm{cal}}
=O\!\left(D^{10}\epsilon_{\mathrm{cal}}^{-2}
\log\frac{D}{\beta}\right)
```

cell exposures, together with an exponentially large data table and a finite-dimensional semidefinite fit. The estimate is intentionally conservative, not a sample-optimal proposal. It makes the cost of an unrestricted certificate explicit.

Compose the fitted physical channel with the nominal isometry and compute or upper-bound

```math
\widehat\epsilon
=\frac12\|\mathcal T_{\mathrm{fit}}\circ\mathcal V_G
-\mathcal N_0\|_\diamond.
```

Then (R2) holds with $`\epsilon=\widehat\epsilon+\epsilon_{\mathrm{cal}}`$, capped at one, on the confidence event. Known preparation, measurement, numerical-fit, and later drift errors must enlarge this radius. Unknown state-preparation and measurement errors cannot simply be removed by fitting the same data; they require independent calibration bounds or a different identifiable model.

For fixed $`B`$ and confidence, the calibration cost is independent of the payload blocklength $`m`$. It is amortizable over many uses only while the channel promise remains valid. If a statement requires total failure probability tending to zero, choose $`\beta_m\to0`$ and include that confidence failure; the logarithmic dependence in (R16) makes, for example, a polynomially small $`\beta_m`$ affordable at fixed $`B`$. A one-time $`99\%`$ confidence statement alone leaves a $`1\%`$ unconditional qualification.

## 5. Endpoint errors and scope of the guarantee

For composed channels, half-diamond error budgets add by the triangle inequality and channel contractivity. Fixed independent cell-level encoding or retrieval imperfections can therefore be included in $`\epsilon`$ before applying Theorem 1. Errors in a collective outer encoder or decoder require a separate block-level guarantee; a constant nonzero total endpoint error leaves a constant fidelity floor instead of the limiting fidelity-one definition of capacity.

The efficient pair task uses an explicit finite endpoint budget, so it does not need asymptotically perfect many-qubit coding. The efficient erasure construction uses ideal or separately certified boundary operations and addresses exactly flagged loss. It does not inherit a decoder for arbitrary coherent calibration residuals or unflagged dephasing merely from continuity.

All strength-independent statements concern the hold interval. Performing a finite-duration gate while an arbitrarily strong unwanted dissipator remains active is a separate control problem. We assume protected or controllable preparation/retrieval windows, or supplied implementations of the stated boundary channels with the charged error. No unbounded-control-rate conclusion follows from a constant gate count.

## References used here

1. I. Bjelaković, H. Boche, and J. Nötzel, *Entanglement transmission and generation under channel uncertainty: Universal quantum channel coding*, Commun. Math. Phys. **292**, 55–97 (2009), [arXiv:0811.4588](https://arxiv.org/abs/0811.4588), Theorem 1.
2. A. Winter, *Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints*, Commun. Math. Phys. **347**, 291–313 (2016), [arXiv:1507.07775](https://arxiv.org/abs/1507.07775), Lemma 2.

The norm estimates, calibration accounting, and applications to the present model are derived above. They are sufficient robustness certificates, not claims of optimal noise thresholds.
