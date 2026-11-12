# A delayed-basis retrieval advantage with imperfect calibration

[Storage model](model.md) · [Robustness](robustness.md) · [Implementation](implementation.md) · [Prior work](prior-work.md)

A fixed two-emitter encoder gives a concrete passive-storage advantage under relative coupling errors, uniform independent loss, an unknown bright-state phase, and additional local dephasing. Its preparation and retrieval use constant-size circuits. The classical comparator may measure the complete challenge register jointly and keep an unlimited classical record.

This is an operational witness for the memory model, not a new BB84 uncertainty theorem or a claim that a two-emitter dark code is new. The separate high-rate contribution is the [capacity cost of arbitrary collective profiles](capacity.md).

## 1. Task and resource interface

A verifier draws independent uniform strings $`X,\Theta\in\{0,1\}^m`$ and supplies

```math
|\psi_{X,\Theta}\rangle
=\bigotimes_{i=1}^{m}H^{\Theta_i}|X_i\rangle.
\tag{O1}
```

The basis string is withheld until the end of a prescribed hold interval. The memory then receives $`\Theta`$ and must return a bit string $`Y`$. It passes when

```math
d_H(X,Y)\le\lfloor\alpha m\rfloor.
\tag{O2}
```

The quantum protocol uses $`2m`$ physical emitters, including one initialized auxiliary emitter per challenge. No original challenge qubit or other quantum system remains available outside these emitters during storage. The verifier's private classical labels are not accessible to the memory. All preparation occurs before the hold, and all decoding and measurements occur after it. No run is removed because of a loss, an unfavorable flag, or a bad answer.

The comparator may apply an arbitrary joint measurement, including arbitrary quantum preprocessing and temporary ancillas, to all $`m`$ challenge states before the hold. It may retain an unlimited classical record, model and calibration information, and independent shared randomness. Preexisting model/calibration data and randomness are independent of the current $`X,\Theta`$; the challenge-dependent retained measurement record may of course depend on the received states. After learning the whole basis string it may perform arbitrary classical computation and prepare fresh ancillas. Every quantum system persisting across the hold would count as quantum memory and is excluded from this comparator.

The task is useful when the later choice of measurement basis must remain available: the device retains a quantum input for a decision made only after storage. It is a retrieval capability, not a computational runtime claim or by itself a complete cryptographic protocol.

## 2. Fixed two-emitter boundary maps

Write

```math
|v\rangle=|00\rangle,\qquad
|D_0\rangle=\frac{|10\rangle-|01\rangle}{\sqrt2},\qquad
|S_0\rangle=\frac{|10\rangle+|01\rangle}{\sqrt2}.
\tag{O3}
```

The encoder $`V_0`$ sends $`|0\rangle`$ to $`|v\rangle`$ and $`|1\rangle`$ to $`|D_0\rangle`$. Use the fixed two-qubit unitary

```math
\begin{aligned}
U_0|00\rangle&=|v\rangle,&
U_0|10\rangle&=|D_0\rangle,\\
U_0|01\rangle&=|S_0\rangle,&
U_0|11\rangle&=|11\rangle.
\end{aligned}
\tag{O4}
```

Thus the encoder applies $`U_0`$ to the input and an auxiliary $`|0\rangle`$. The decoder applies $`U_0^\dagger`$ and discards the second emitter. Its action is a completely positive trace-preserving map on the full four-dimensional space: the vacuum and $`S_0`$ yield logical zero, while $`D_0`$ and $`|11\rangle`$ yield logical one, with coherences determined by the stated unitary and partial trace. The model never populates $`|11\rangle`$, but its completion is specified.

Chronologically, an implementation of $`U_0`$ is CNOT from emitter 1 to emitter 2, controlled-$`R_y(\pi/2)`$ on emitter 1 controlled by emitter 2, and the same CNOT again. The controlled rotation decomposes into two CNOTs and two one-qubit rotations. Each encoding or decoding therefore uses at most four CNOTs and two fixed one-qubit rotations. The final basis measurement is $`Z`$ for $`\Theta_i=0`$ and $`X`$ for $`\Theta_i=1`$.

These gates assume protected or controllable preparation and retrieval windows, or supplied boundary channels with the error budget used below. Their constant count is not a proof that finite-duration gates work while an unbounded unwanted collective dissipator remains active.

## 3. Exact channel with a misaligned collective mode

During the hold, let the actual static collective jump be

```math
L=g_1\sigma_1^-+g_2\sigma_2^-,\qquad
\Gamma=|g_1|^2+|g_2|^2>0.
\tag{O5}
```

Both emitters also have the same independent-loss rate $`\kappa`$, with $`\eta=e^{-\kappa t}`$. In the single-excitation sector let $`P_B`$ be the rank-one bright projector of $`L^\dagger L`$ and $`P_D=I-P_B`$. Define the calibration leakage

```math
b=\langle D_0|P_B|D_0\rangle
=\frac{|g_1-g_2|^2}{2\Gamma}.
\tag{O6}
```

Allow an unknown static bright-state Hamiltonian $`H_B=\omega_B P_B`$. The vacuum and actual dark state have the same known energy in the chosen rotating frame. A separate uncontrolled vacuum-to-dark phase is discussed below.

The no-jump operator in this sector is

```math
F=\sqrt\eta\,(P_D+zP_B),\qquad
z=e^{-\Gamma t/2-i\omega_Bt},\qquad |z|\le1.
\tag{O7}
```

Every collective or local lowering jump from this sector ends in the vacuum. Consequently, after the fixed decoder, the channel on the logical qubit has survival amplitude

```math
A=\langle D_0|F|D_0\rangle
=\sqrt\eta\,(1-b+bz).
\tag{O8}
```

Explicitly,

```math
\begin{pmatrix}\rho_{00}&\rho_{01}\\\rho_{10}&\rho_{11}\end{pmatrix}
\longmapsto
\begin{pmatrix}
\rho_{00}+(1-|A|^2)\rho_{11}&A^*\rho_{01}\\
A\rho_{10}&|A|^2\rho_{11}
\end{pmatrix}.
\tag{O9}
```

To check (O9), resolve $`F|D_0\rangle`$ into the nominal $`D_0,S_0`$ basis. The former component becomes a logical excitation with auxiliary zero; the latter becomes logical zero with auxiliary one. Tracing that auxiliary removes their cross term. Jump branches also contribute logical zero. Vacuum-to-$`D_0`$ coherence has exactly the amplitude (O8).

When $`\omega_B=0`$, $`A`$ is real and

```math
|A|^2=\eta\left[1-b(1-e^{-\Gamma t/2})\right]^2
\ge\eta(1-b)^2.
\tag{O10}
```

With an arbitrary bright phase and $`b\le1/2`$, a uniform bound is

```math
\operatorname{Re}A\ge\sqrt\eta(1-2b),\qquad
|A|^2\ge\eta(1-2b)^2.
\tag{O11}
```

The bound follows from $`\operatorname{Re}z\ge-1`$ and
$`|1-b+bz|\ge1-b-b|z|\ge1-2b`$.
It is independent of the collective strength and of the bright phase accumulated during the hold.

### Sharp conversion from coupling error to leakage

**Lemma 1.** Suppose $`g_0\ne0`$ and the two complex couplings obey

```math
|g_j-g_0|\le\delta|g_0|,\qquad j=1,2,\qquad 0\le\delta<1.
\tag{O12}
```

Then $`b\le\delta^2`$, and the bound is attainable.

**Proof.** Put $`u=(g_0,g_0)`$ and $`g=(g_1,g_2)`$. Condition (O12) implies
$`\|g-u\|\le\delta\|u\|`$.
The distance from $`u`$ to the complex line spanned by $`g`$ cannot exceed its distance to the particular point $`g`$ on that line. Hence

```math
1-\frac{|u^\dagger g|^2}{\|u\|^2\|g\|^2}
\le\delta^2.
```

The left side is
$`1-|g_1+g_2|^2/(2\Gamma)=|g_1-g_2|^2/(2\Gamma)=b`$.
For equality, take

```math
\frac{g_{1,2}}{g_0}
=1-\delta^2\,\pm i\delta\sqrt{1-\delta^2}.
\tag{O13}
```

Each deviation has modulus $`\delta`$, and substitution gives $`b=\delta^2`$. $`\square`$

Thus this uncertainty model does not require the weaker replacement $`\delta^2/(1-\delta)^2`$. The nominal encoder and decoder require no estimate of the actual complex direction within (O12).

## 4. BB84 error and additional dephasing

For the channel (O9), the average error on uniformly chosen computational-basis bits is $`(1-|A|^2)/2`$. The average error on uniformly chosen Hadamard-basis bits is $`(1-\operatorname{Re}A)/2`$. Their uniform average is

```math
p_{\mathrm{pair}}
=\frac{2-|A|^2-\operatorname{Re}A}{4}.
\tag{O14}
```

For $`\delta^2\le1/2`$, (O11) and Lemma 1 imply

```math
p_{\mathrm{pair}}
\le p_0(\eta,\delta)
:=\frac{2-\eta(1-2\delta^2)^2
-\sqrt\eta(1-2\delta^2)}4.
\tag{O15}
```

Now add in-storage local dephasing

```math
\mathcal R_\phi(s)
=\nu_1(s)\mathcal D[Z_1]+\nu_2(s)\mathcal D[Z_2],
\qquad \nu_j(s)\ge0.
\tag{O16}
```

Since $`\mathcal D[Z](\rho)=Z\rho Z-\rho`$ has diamond norm two, the propagator estimate in [Robustness](robustness.md) gives

```math
\epsilon_\phi
\le\min\!\left\{1,\sum_{j=1}^2\int_0^t\nu_j(s)\,ds\right\}.
\tag{O17}
```

This treats dephasing during the hold itself, including subsequent collective loss of any bright component it creates. It does not replace dephasing by a commuting terminal channel. The bound is uniform in $`\Gamma`$ and $`\omega_B`$.

Let $`\epsilon_{\mathrm{other}}`$ bound any remaining hold-channel perturbation in half-diamond norm, and let $`\epsilon_{\mathrm{end}}`$ be the sum of certified preparation, decoding, and basis-readout errors relative to the stated boundary channels. Contractivity and the operational meaning of trace distance imply

```math
p\le p_*:=p_0(\eta,\delta)
 +\epsilon_\phi+\epsilon_{\mathrm{other}}+\epsilon_{\mathrm{end}}.
\tag{O18}
```

The final classical output is included in this distance statement, so an additive channel budget bounds the error probability for the actual task directly. The comparison is useful whenever $`p_*`$ is below the classical threshold specified next.

## 5. Classical bound, including joint initial measurements

Define

```math
\gamma_*:=\frac{1-1/\sqrt2}{2}
=0.1464466094\ldots,
\qquad
D_2(a\|b)=a\log_2\frac ab
 +(1-a)\log_2\frac{1-a}{1-b}.
\tag{O19}
```

**Theorem 2 — Classical retained-record bound.** Every classical-memory strategy allowed in Section 1 satisfies, for $`0\le\alpha<\gamma_*`$,

```math
\Pr_{\mathrm{classical}}[\mathrm{pass}]
\le2^{-mD_2(\alpha\|\gamma_*)}.
\tag{O20}
```

**Reduction to the existing theorem.** Replace each prepared BB84 challenge by one half of an EPR pair and defer the verifier's basis measurement on the other half. The real BB84 bases are real matrices, so this produces exactly the challenge ensemble (O1), with the same joint distribution of retained data and labels. After the comparator's arbitrary joint initial instrument, only a classical record remains. Copy that record, including any independent random seed, to two separated players. Both receive $`\Theta`$ and execute the same classical decoding rule. Their answers are always identical and have exactly the comparator's error pattern.

This is an admissible identical-answer BB84 monogamy-game strategy, even though the initial measurement was collective and its record arbitrarily large. Theorem 3, equation (7), of [Escolà-Farràs and Speelman, arXiv:2611.09504v2](https://arxiv.org/html/2611.09504v2) gives (O20). Their finite-size refinement uses $`\lfloor\alpha m\rfloor/m`$ in place of $`\alpha`$ and is at least as strong. The underlying error-free parallel-repetition theorem is due to [Tomamichel, Fehr, Kaniewski, and Wehner (2013)](https://doi.org/10.1088/1367-2630/15/10/103002). $`\square`$

The threshold and asymptotic exponent are sharp for this comparator: independent Breidbart measurements give a classical error rate $`\gamma_*`$ and the corresponding binomial lower-tail exponent. Our result imports this bound; the new physical calculation concerns how the passive pair stays below its threshold.

For independent quantum cells with bit-error probabilities $`p_i\le p_*<\alpha`$, the ordinary exponential-moment bound gives

```math
\Pr_{\mathrm{quantum}}[\mathrm{pass}]
\ge1-2^{-mD_2(\alpha\|p_*)}.
\tag{O21}
```

The $`p_i`$ need not be identical. The inequality follows from
$`\mathbb E e^{s\sum_i E_i}\le(1-p_*+p_*e^s)^m`$ for independent bit-error indicators and $`s\ge0`$. In fact it is enough that the mean $`\overline p=m^{-1}\sum_i p_i`$ is at most $`p_*`$: concavity of $`p\mapsto\ln(1-p+pe^s)`$ bounds the product moment generating function by its value at $`\overline p`$. Static coupling parameters may differ between pairs. A uniform physical promise, paid per-cell calibration, or the uniformly sampled-array protocol in [Robustness](robustness.md) can supply the relevant error bound; testing an arbitrary single pair does not supply it. Cross-pair dynamical noise correlations are not included in (O21).

Together, (O20)–(O21) give an exponentially reliable quantum-versus-classical separation whenever

```math
p_*<\alpha<\gamma_*.
\tag{O22}
```

## 6. An endpoint-inclusive finite working point

Take the following dimensionless parameters.

| Quantity | Value | Meaning |
| --- | --- | --- |
| Independent survival $`\eta`$ | $`0.90`$ | $`\kappa t=-\ln0.9`$ on each emitter |
| Coupling uncertainty $`\delta`$ | $`0.10`$ | Complex relative error in each coupling; $`b\le0.01`$ |
| Bright-state phase | Arbitrary static value | No phase estimation in the encoder or decoder |
| Dephasing exposure per emitter | $`\int_0^t\nu_j(s)\,ds=0.01`$ | Total certified contribution at most $`0.02`$ |
| Total endpoint half-diamond error | $`0.01`$ | Includes preparation, decoding, and readout |
| Other hold error | $`0`$ in this example | A further error can use the remaining strict margin |
| Accepted error fraction $`\alpha`$ | $`0.10`$ | Every answer is counted |

Equation (O15) gives

```math
p_0=0.05148259198\ldots,
\qquad
p_*=0.08148259198\ldots<0.10<\gamma_*.
\tag{O23}
```

Writing the binary relative entropy in natural logarithms as $`D_e=(\ln2)D_2`$,

```math
D_e(0.10\|p_*)=0.002148593958\ldots,
\qquad
D_e(0.10\|\gamma_*)=0.009538927833\ldots.
\tag{O24}
```

For $`m=2200`$ parallel independent pairs, hence $`4400`$ physical emitters, the conservative finite bounds are

```math
\Pr_{\mathrm{quantum}}[\mathrm{pass}]\ge0.99114618,
\qquad
\Pr_{\mathrm{classical}}[\mathrm{pass}]
\le7.69223\times10^{-10}.
\tag{O25}
```

The pair circuits use a number of boundary gates linear in $`m`$; storage uses no gates or measurements. These numbers are conditional on the stated physical and endpoint certificates. If those certificates are learned with finite confidence, the calibration failure probability must be included separately as described in [Robustness](robustness.md). The numerical margin does not constitute an experimental observation.

## 7. Phase, drift, and lifetime limits

An unknown phase between the vacuum and the actual dark state is different from the bright phase in (O7). If a common emitter frequency contributes a residual phase $`\phi`$, the survival amplitude acquires a factor $`e^{-i\phi}`$. Arbitrarily unknown $`\phi`$ removes the uniform $`X`$-basis advantage. A known rotating frame, a calibrated terminal phase correction, or an explicit phase budget is therefore required for this cross-excitation pair code.

For example, if $`|\phi|\le\phi_{\max}\le\pi`$, then

```math
\operatorname{Re}(e^{-i\phi}A)
\ge\sqrt\eta\bigl[(1-b)\cos\phi_{\max}-b\bigr],
\tag{O26}
```

while the magnitude bound is unchanged. Substitution in (O14) gives the corresponding additional phase tolerance. The fixed-excitation erasure code in [Implementation](implementation.md) is insensitive to an unknown common excitation phase because it is global on every surviving codeword.

The direction of $`g`$ is static during each hold in the exact calculation. Bounds on its total variation can instead enter a perturbation budget, but an arbitrarily drifting direction is not covered by the geometric argument alone. Generic frequency disorder, thermal excitation, nonuniform independent damping, and intercell reservoirs also require their own declared error bounds.

Finally, nonzero independent loss sets a finite storage horizon. In the exact dark-input capacity model, positive unassisted capacity requires $`\eta>1/2`$, equivalently $`\kappa t<\ln2`$ for $`\kappa>0`$. The explicit uncoded pair task imposes its stronger score requirement (O22). No infinite-time or self-correcting-memory claim follows from removing collective decay.

## Primary references for the comparator

1. L. Escolà-Farràs and F. Speelman, *Sharp error tolerance of the monogamy-of-entanglement game*, [arXiv:2611.09504v2](https://arxiv.org/html/2611.09504v2), Theorem 3 and equations (7)–(9). The full primary text was used for the tolerated-error exponent.
2. M. Tomamichel, S. Fehr, J. Kaniewski, and S. Wehner, *A monogamy-of-entanglement game with applications to device-independent quantum cryptography*, New J. Phys. **15**, 103002 (2013), [DOI:10.1088/1367-2630/15/10/103002](https://doi.org/10.1088/1367-2630/15/10/103002).

The classical exponent is an existing theorem. Equations (O8)–(O18) and their endpoint-inclusive use here are the physical task calculation.
