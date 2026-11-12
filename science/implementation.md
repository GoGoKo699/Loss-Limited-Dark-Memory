# Boundary circuits and a positive-rate erasure construction

[Storage model](model.md) · [Capacity theorem](capacity.md) · [Robustness](robustness.md) · [Operational advantage](operational-advantage.md)

The high-rate capacity theorem does not supply efficient encoders and decoders. Two smaller constructions make the endpoint costs explicit: the fixed pair circuit for robust delayed-basis retrieval, and a single-excitation dark code followed by an efficiently sampled stabilizer erasure code. The latter stores arbitrary quantum data at positive rate with correction only after storage. Its rate is below the full amplitude-damping benchmark, and its decoder corrects flagged loss under the stated exact erasure model.

## 1. Boundary-operation interface

Encoding takes place before a prescribed hold interval of duration $`t`$; recovery takes place after it. During the hold, every device-accessible quantum system is one of the counted physical emitters. There is no retained original payload, external protected register, preshared entanglement supply, syndrome measurement, feedback, reset, or fresh quantum ancilla during that interval.

Boundary windows must be protected or controllable, or the corresponding preparation and retrieval channels must be supplied with certified errors. A gate-count bound does not guarantee a finite-duration gate under arbitrarily strong always-on decay. The present results assume available boundary operations; they do not establish the hardware control mechanism that makes those operations accurate.

For finite pair tasks, the endpoint error is a fixed charged part of the bit-error budget. For asymptotically reliable coding, ideal boundary operations, or boundary implementations with total error tending to zero, are required. Fault-tolerant implementation under noisy gates is a separate question. Connectivity is unrestricted in the gate counts below; geometrical routing, clock time, and control bandwidth can add costs.

## 2. Constant-size robust pair endpoints

The two-emitter isometry and its complete decoder are specified in [Operational advantage](operational-advantage.md), equations (O3)–(O4). Each boundary uses at most four CNOTs and two fixed one-qubit rotations; the decoder discards one emitter and measures the other in the revealed basis. Its gate pattern does not depend on the unknown actual coupling direction or bright phase.

For $`m`$ challenges, this protocol uses $`2m`$ emitters and $`O(m)`$ boundary gates and measurements. No outer error-correcting code is needed for the tolerated-error task. Relative coupling errors, added local dephasing, endpoint noise, and the classical comparator are all included in that page's explicit finite probability bounds.

## 3. A single-excitation dark cell is exactly an erasure channel

For a rank-$`r`$ profile matrix $`G\in\mathbb C^{r\times B}`$, the one-excitation sector is naturally $`\mathbb C^B`$. The collective lowering map on that sector is exactly the matrix $`G`$, so

**(I1)**

```math
\dim\mathcal K_{G,1}=B-r.
```

Here $`r`$ is the actual row rank of the supplied span, not the number of possibly redundant listed modes. Select an orthonormal $`d`$-dimensional subspace

**(I2)**

```math
\mathcal C\subseteq\mathcal K_{G,1},
\qquad 2\le d\le B-r.
```

Every codeword contains exactly one excitation. The vacuum $`|v\rangle=|0\cdots0\rangle`$ is orthogonal to the entire code.

**Proposition 1 — Exact flagged channel.** Under uniform independent survival $`\eta=e^{-\kappa t}`$ and the collective model of [Model](model.md), the physical channel on $`\mathcal C`$ is

**(I3)**

```math
\mathcal E_\eta(\rho)
=\eta\rho+(1-\eta)|v\rangle\langle v|\mathrm{Tr}\rho.
```

With a final isometry identifying $`\mathcal C`$ with a $`d`$-level register and the vacuum with an orthogonal erasure flag, this is the ordinary $`d`$-dimensional quantum erasure channel.

**Proof.** The no-loss Kraus operator is $`\sqrt\eta I`$ on the single-excitation sector. Each nonzero loss branch is
$`\sqrt{1-\eta}|v\rangle\langle j|`$, where $`|j\rangle`$ denotes the excitation at site $`j`$. Summing its action over $`j`$ gives
$`(1-\eta)|v\rangle\langle v|\mathrm{Tr}\rho`$.
All collective jumps annihilate $`\mathcal C`$, and every local loss ends in the vacuum, which is also dark. The simultaneous evolution therefore has exactly these branches. The argument applies to every encoded matrix unit and to reference-entangled inputs, proving a channel equality. $`\square`$

The loss probability is independent of the logical state. Measuring only whether the output is vacuum consequently reveals a loss flag without measuring the surviving logical data. All erasures are kept in the record and handled by the outer decoder.

An arbitrary unknown common excitation phase acts as a global phase on the surviving code subspace and has no effect on (I3). Collective coefficients and their time dependence can also be unknown if all actual modes remain inside the supplied span. These are exact calibration tolerances. An unknown Hamiltonian acting nontrivially within the selected dark subspace is a different error.

The unassisted capacity of (I3) is

**(I4)**

```math
Q(\mathcal E_\eta)
=\max\{0,2\eta-1\}\log_2d.
```

This is the established erasure-channel capacity of [Bennett, DiVincenzo, and Smolin (1997)](https://arxiv.org/abs/quant-ph/9701015), with the elementary $`d`$-dimensional extension. It is an unassisted storage rate: the receiver reads flags only after the hold. A two-way-assisted communication rate would be a different resource interface.

After charging all $`B`$ emitters per cell, the achievable rate is

**(I5)**

```math
R_{\mathrm{erase}}
=\frac{\log_2d}{B}\max\{0,2\eta-1\}.
```

For an elementary binary implementation choose $`d=2^\ell\le B-r`$, with $`\ell=\lfloor\log_2(B-r)\rfloor`$. Each cell then carries $`\ell`$ outer-code qubits, all erased together on a loss. A selected smaller power of two is also allowed. When $`B-r\lt 2`$, this construction has no nontrivial logical cell. It makes no claim of positive rate at those parameters merely from the presence of a one-dimensional dark state.

## 4. An explicit three-emitter qubit

For one supplied uniform collective profile, $`B=3,r=1`$, use

**(I6)**

```math
|0_L\rangle=\frac{|100\rangle-|010\rangle}{\sqrt2},
\qquad
|1_L\rangle=\frac{|100\rangle+|010\rangle-2|001\rangle}{\sqrt6}.
```

Both coefficient vectors sum to zero, so every unknown scalar multiple of $`\sigma_1^-+\sigma_2^-+\sigma_3^-`$ annihilates them. They are orthonormal. Their span is the full two-dimensional dark single-excitation sector.

For an explicit encoder, let $`G_{ab}(\theta)`$ be a number-preserving two-emitter rotation whose single-excitation action is

**(I7)**

```math
\begin{aligned}
G_{ab}(\theta)|a\rangle
 &=\cos\theta\,|a\rangle-\sin\theta\,|b\rangle,\\
G_{ab}(\theta)|b\rangle
 &=\sin\theta\,|a\rangle+\cos\theta\,|b\rangle,
\end{aligned}
```

and which fixes $`|00\rangle`$ and $`|11\rangle`$ on that pair. Here $`|a\rangle`$ denotes the excitation at site $`a`$. Put $`\theta=\arccos(1/\sqrt3)\in(0,\pi/2)`$. Starting with an input on emitter 1 and emitters 2 and 3 in zero, apply chronologically

1. $`X`$ on emitter 2;
2. CNOT from emitter 1 to emitter 2;
3. SWAP of emitters 1 and 2;
4. $`G_{23}(\theta)`$;
5. $`G_{12}(\pi/4)`$.

Call the resulting unitary $`W`$. The first three gates send logical zero and one to an excitation at site 1 and site 2 respectively. The final rotations send them to (I6). Each rotation is a fixed two-qubit gate and has a constant-size elementary decomposition, so the whole encoder is constant size in a gate model allowing specified one- and two-qubit rotations. Synthesis to a discrete universal gate set has an additional accuracy cost, included in the endpoint error and work budgets.

The decoder applies $`W^\dagger`$. A surviving codeword becomes the input qubit on emitter 1 with emitters 2 and 3 both zero. The erasure vacuum instead becomes

**(I8)**

```math
W^\dagger|000\rangle=|010\rangle.
```

Measuring emitter 2 therefore reads the erasure flag without disturbing surviving logical data. Emitters 2 and 3 can then be discarded. This specifies a physical decoder on the whole three-emitter space through a unitary and measurements, even though only the code and vacuum are reached in the exact model.

At $`\eta=0.9`$, (I5) is $`0.8/3=0.2666\ldots`$ logical qubits per physical emitter. Every strictly smaller rate is achievable by the outer construction below; for example, rate $`0.2`$ per emitter is a valid positive-rate choice. This number includes all three emitters and does not assert efficient attainment of the larger general dark-input amplitude-damping capacity.

## 5. Efficient final-only stabilizer recovery

For completeness, a direct random-stabilizer argument gives a constructive coding guarantee and its decoder costs. It avoids relying on an unproved efficient decoder for a general amplitude-damping channel.

Use $`m`$ independent erasure cells of dimension $`d=2^\ell`$. Put $`n=m\ell`$ for the number of binary outer-code carriers before their inner embedding, and let $`k`$ be the unknown logical-qubit payload. Let the loss probability of each cell be at most $`\lambda\lt 1/2`$, with losses independent of the payload and independent across cells. The cell channels may be nonidentical, provided they remain exact flagged erasure channels with this uniform upper bound.

Sample a uniform $`[[n,k]]`$ stabilizer code by conjugating a standard stabilizer with a uniform Clifford. Its classical description and the random seed are independent of the current payload. A uniformly random symplectic basis can be sampled by sequential linear algebra over $`\mathbb F_2`$; the stabilizer and a Clifford encoding circuit can be stored and operated in polynomial time.

**Lemma 2 — Random-code erasure bound.** For a fixed set of $`e`$ erased cells, the probability over the sampled stabilizer code that this erasure pattern is uncorrectable satisfies

**(I9)**

```math
\Pr_{\mathrm{code}}[\mathrm{failure}\mid e]
\le\min\left\{1,
(2^{2\ell e}-1)\frac{2^{n+k}-1}{2^{2n}-1}\right\}
\le\min\{1,2^{\,2\ell e-(n-k)+1}\}.
```

**Proof.** A stabilizer erasure pattern is correctable exactly when every Pauli supported on the erased qubits that commutes with all stabilizers belongs to the stabilizer. For a fixed nonidentity Pauli, symplectic invariance gives probability
$`(2^{n+k}-1)/(2^{2n}-1)`$ of lying in the normalizer of a uniformly random stabilizer, ignoring phases. There are $`2^{2\ell e}-1`$ nonidentity Paulis supported on the erased qubits. A union bound over this larger normalizer event proves (I9). Counting stabilizers themselves as failures only weakens the bound, so degeneracy does not invalidate it. $`\square`$

Let $`R=k/m`$ be the number of logical qubits per cell. Choose any $`a>0`$ such that

**(I10)**

```math
R\lt \ell\,[1-2(\lambda+a)].
```

An exponential-moment bound for the independent loss flags, followed by (I9), gives

**(I11)**

```math
\mathbb E_{\mathrm{code}}P_{\mathrm{fail}}
\le\epsilon_m
:=e^{-mD_e(\lambda+a\|\lambda)}
 +2^{\,1-m\{\ell-R-2\ell(\lambda+a)\}}.
```

For nonidentical loss probabilities at most $`\lambda`$, their moment generating function is bounded by that of a binomial variable with parameters $`m,\lambda`$, giving the same first term. Correctable patterns recover every logical state exactly, including its entanglement with a reference, so the average entanglement fidelity is at least $`1-\epsilon_m`$.

Every $`R\lt \ell(1-2\lambda)`$ admits an $`a`$ satisfying (I10), proving the rate (I5) for binary cells. Markov's inequality also shows that all but at most a $`\sqrt{\epsilon_m}`$ fraction of sampled codes have failure probability at most $`\sqrt{\epsilon_m}`$. Thus this is an efficiently sampled and operated code ensemble with an exponentially improving performance guarantee. The argument does not give a polynomial certificate that a particular sampled code is good for every likely erasure pattern; it supplies an average guarantee and the stated high-probability conclusion.

### Encoding and recovery operations

Encode the $`k`$ payload qubits and $`n-k`$ initialized ancillary qubits by the sampled Clifford, then apply the fixed inner isometry on each cell. No quantum data is retained outside the $`mB`$ emitters. At retrieval:

1. Apply each inner decoder and measure its erasure flag.
2. Replace erased logical carriers by maximally mixed qubits. This is equivalent to uniformly averaging Pauli errors supported on the erased positions.
3. Measure the stabilizer generators at this final boundary.
4. Solve the binary linear syndrome equations for a Pauli supported on the known erased positions, apply that correction, and invert the Clifford encoder.

On a correctable erasure pattern, any two syndrome-consistent candidate errors differ by a stabilizer, so the recovered logical state is independent of the chosen solution. If the pattern is uncorrectable, it may be flagged as failure; its probability remains included in (I11), rather than being postselected out of the rate or fidelity.

Binary Gaussian elimination tests correctability and finds a correction with a conservative $`O(n^3)`$ classical-operation bound. A stabilizer tableau and the retained code description use $`O(n^2)`$ classical bits. Clifford synthesis and dense stabilizer measurements require at most $`O(n^2)`$ elementary gates with unrestricted connectivity; [Aaronson and Gottesman (2004)](https://arxiv.org/abs/quant-ph/0406196) give a stronger general Clifford-synthesis bound. Syndrome ancillas can be introduced and reset at the final boundary. They are not long-lived memory carriers.

For fixed $`B,d`$, the inner isometries have fixed finite compilation cost, and the total number of physical storage emitters is $`mB`$. The explicit three-emitter construction avoids any unspecified inner compilation. We do not claim a uniformly efficient circuit for the arbitrary many-excitation dark Gibbs codes underlying the near-$`Q_{\mathrm{AD}}`$ theorem.

## 6. A quantum-data witness with the same endpoints

The erasure construction stores arbitrary quantum inputs. To witness this operationally, an inaccessible verifier prepares $`k`$ Bell pairs, supplies one half of each to the memory, and keeps the other halves as references. After retrieval it tests the $`k`$ output-reference pairs against the maximally entangled state. The quantum acceptance probability is the entanglement fidelity and is at least $`1-\epsilon_m`$ for the randomized construction above.

Any memory carrying only a classical record across the hold implements an entanglement-breaking channel, even if its initial measurement is joint and its classical record unlimited. Its reference-output state is separable. For a maximally entangled state of dimension $`2^k`$, every product state's squared overlap is at most $`2^{-k}`$ by Cauchy–Schwarz; convexity gives the same bound for every separable state. Thus

**(I12)**

```math
\Pr_{\mathrm{classical}}[\mathrm{Bell\ test\ passes}]
\le2^{-k}.
```

The reference system belongs only to the verifier and supplies no assistance to the memory during storage. Bell-pair preparation and final Bell measurements add $`O(k)`$ verifier gates; their trusted errors must be included if this is implemented as an experiment. The memory's Clifford and inner-code costs are those charged above.

## 7. Calibration and imperfections: the boundary of this construction

The single-excitation code requires the supplied dark span or an exactly specified inner subspace. Unknown magnitudes and mixtures of collective modes within that span, and an unknown common excitation phase, do not change (I3). Uniform independent amplitude damping is an additional physical noise process included exactly, not a perturbative assumption of vanishing local loss.

By contrast, a generic error in the spatial span can leave an unflagged coherent distortion on surviving codewords. Local dephasing can also create unflagged logical errors. Nonuniform local damping can make the no-jump survival operator depend on the logical state. An erasure-only decoder is not, without another argument, a decoder for those channels. The robust pair witness already tolerates explicit direction error and dephasing; the compound theorem gives an information-theoretic common-code guarantee for more general finite-cell perturbations. These results should not be combined into an unproved efficient near-capacity noisy decoder.

Calibration acquisitions are charged in [Robustness](robustness.md). In particular, testing one stationary pair procedure does not certify every member of a heterogeneous parallel array. The nonidentical-cell extensions require uniform manufacturing/parameter bounds, separately paid per-cell calibration, or another justified inference controlling the required error probabilities. For the pair task, that page supplies an explicit uniformly sampled-array protocol certifying the mean error, which is sufficient for its independent-pair concentration bound. Code and calibration records used during a payload task are independent of that task's hidden data.

Positive unassisted storage rate in this exact construction requires $`\eta>1/2`$, or $`\kappa t\lt \ln2`$ for nonzero $`\kappa`$. This is a loss-limited finite-time memory, not an infinite-lifetime passive memory. The capacity statement and the endpoint construction make no claim that arbitrarily noisy preparation or recovery can be omitted from the resource accounting.

## Resource summary

| Construction | Physical emitters | Boundary quantum work | Classical work | Noise/calibration scope |
| --- | --- | --- | --- | --- |
| Robust pair task on $`m`$ challenges | $`2m`$ | $`O(m)`$ fixed gates and final basis measurements | $`O(m)`$ task processing, plus paid calibration | Static relative direction error; arbitrary bright phase; quantified dephasing and endpoint error |
| Erasure code on $`m`$ fixed cells | $`mB`$ | $`O((m\ell)^2)`$ outer gates plus fixed per-cell maps | $`O((m\ell)^3)`$ conservative decoding, $`O((m\ell)^2)`$ code storage | Exact known-span dark code; uniform independent loss; independent flags |
| General compound-capacity code | $`mB`$ | Information-theoretic existence; no efficient bound supplied | Calibration can be exponential in $`B`$ | A fixed unknown cell channel repeated independently within a certified radius |

All three rows have no control or measurement during the hold. Preparation, retrieval, calibration exposures, and any needed routing or boundary error suppression are additional charged resources rather than hidden storage.

## Primary coding references

1. C. H. Bennett, D. P. DiVincenzo, and J. A. Smolin, *Capacities of Quantum Erasure Channels*, Phys. Rev. Lett. **78**, 3217–3220 (1997), [arXiv:quant-ph/9701015](https://arxiv.org/abs/quant-ph/9701015), equation (2).
2. D. Gottesman, *Stabilizer Codes and Quantum Error Correction*, Ph.D. thesis (1997), [arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052), for the stabilizer error-correction formalism.
3. S. Aaronson and D. Gottesman, *Improved Simulation of Stabilizer Circuits*, Phys. Rev. A **70**, 052328 (2004), [arXiv:quant-ph/0406196](https://arxiv.org/abs/quant-ph/0406196), for tableau methods and efficient Clifford synthesis.

The explicit random-code counting bound (I9)–(I11) and the inner-cell circuit are written out to state exactly which coding efficiency and physical assumptions are used.
