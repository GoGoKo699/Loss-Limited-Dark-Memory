# From Wilde's channels to loss-limited dark memory

[Scientific account](../science/README.md) · [Milestone map](milestones.md) · [Research references](../references/README.md)

An unknown qubit must remain available until a later measurement or computation. During the waiting interval, its physical emitters can radiate into a shared environment and can also decay independently. A dark encoding uses destructive interference to remove the shared decay. Independent decay remains, so a dark space's dimension alone does not tell us how much information can be recovered.

This project connects that physical distinction to quantum channel capacity. Its central result bounds the additional rate penalty imposed by collective darkness when local loss is already present. A smaller explicit construction turns local loss into detectable erasures; a different pair construction demonstrates a robust delayed-measurement advantage. These results share physical ingredients but answer different operational questions.

## 1. The selected source and a focused reading map

The educational anchor is Mark M. Wilde, *From Classical to Quantum Shannon Theory*, [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), posted 14 July 2019: the author draft associated with *Quantum Information Theory*, second edition (2017). The locators below follow [that exact draft](https://arxiv.org/pdf/1106.1445v8), rather than assuming identical pagination in another edition.

| Draft location | Connection to this project |
| --- | --- |
| §4.7, **Examples of Quantum Channels** | Identify amplitude damping and distinguish it from flagged erasure. |
| §11.5, **Coherent Information** | Connect preservation of an unknown input to its reference correlations. |
| §11.8, **Quantum Relative Entropy** | Compare the dark input with the capacity-optimal product input. |
| §13.5, **Coherent Information of a Quantum Channel** | Understand degradability, additivity, and input optimization. |
| Chapter 24, **Quantum Communication** | Interpret a capacity as a coding limit over repeated uses. |
| §24.7.1, **The Quantum Erasure Channel** | Read the rate of the explicit single-excitation construction. |
| §24.7.2, **The Amplitude Damping Channel** | Identify the independent-loss benchmark. |

The following derivations connect those tools to the project's particular emitter model. Complete proofs and primary research attribution remain in the linked scientific pages. The source supplies the information-theoretic framework; it is not a source for the weighted dark-kernel theorem.

## 2. Translate the symbols before translating the result

The important parameter conversion is between loss and survival. If the source's amplitude-damping probability is $`\gamma`$, this project uses $`\eta=1-\gamma`$. Thus $`\eta=0.9`$ means ten percent loss, not ninety percent loss.

| Symbol here | Meaning and translation |
| --- | --- |
| $`B`$ | Number of physical emitters in one cell; not an output-system label. |
| $`R,Y,E`$ | Untouched reference, receiver output, and channel environment. |
| $`S(\rho)`$ | Quantum entropy in bits; the source also uses $`H`$ for entropy. |
| $`\mathcal A_\eta`$ | One-emitter amplitude damping with survival $`\eta`$. |
| $`G,r`$ | Supplied spatial profile matrix and its actual row rank. |
| $`K_G,P_G`$ | Common dark space and its orthogonal projector. |
| $`D(\rho\Vert\sigma)`$ | Quantum relative entropy comparing an input with a reference state. |
| $`I_c(\rho,\mathcal N)`$ | Coherent information at one specified input. |
| $`Q_{\mathrm{dark}}(G,\eta)`$ | Asymptotic qubits per cell with inputs constrained to $`K_G`$. |

A reference is a mathematical way to test whether unknown quantum information survives. It is inaccessible to the memory and does not provide the memory with another protected copy. A code using $`m`$ cells occupies all $`mB`$ emitters, including initialized redundancy. Dividing a rate per cell by $`B`$ is therefore essential.

The model also fixes the time interface. Encoding precedes a hold of duration $`t`$; recovery follows it. There are no measurements, resets, fresh ancillas, or feedback during the hold. Joint recovery at the end is allowed. “Passive” describes this interval, not an absence of encoding and decoding work.

## 3. A complete three-emitter example

Take one supplied collective profile,

```math
L=a_1+a_2+a_3,\qquad
a_j=|0\rangle\langle1|_j.
```

On a single-excitation state, $`L`$ adds the three excitation amplitudes and sends their sum to the vacuum. The following orthonormal states both have coefficient sum zero:

```math
|0_L\rangle
=\frac{|100\rangle-|010\rangle}{\sqrt2},
```

```math
|1_L\rangle
=\frac{|100\rangle+|010\rangle-2|001\rangle}{\sqrt6}.
```

Every superposition $`\alpha|0_L\rangle+\beta|1_L\rangle`$ is dark. An unknown scalar multiplying $`L`$ does not change this statement. Both codewords contain exactly one excitation, so an unknown common excitation phase is global on the surviving code.

### Encoding and reading the flag

The [explicit boundary circuit](../science/implementation.md#4-an-explicit-three-emitter-qubit) starts with the unknown qubit on emitter 1 and emitters 2 and 3 in their ground states. It first applies $`X_2`$, CNOT from 1 to 2, and SWAP of 1 and 2. The two input basis states have now become excitations at site 1 and site 2.

Two number-preserving pair rotations complete the encoding. A rotation $`G_{ab}(\theta)`$ acts on the two excitation locations as

```math
\begin{aligned}
|a\rangle&\mapsto
\cos\theta\,|a\rangle-\sin\theta\,|b\rangle,\\
|b\rangle&\mapsto
\sin\theta\,|a\rangle+\cos\theta\,|b\rangle.
\end{aligned}
```

Each rotation fixes the vacuum and the double-excitation state of its pair. Apply $`G_{23}(\arccos(1/\sqrt3))`$, followed by $`G_{12}(\pi/4)`$. The resulting unitary $`W`$ gives the two codewords above. This is a fixed-size circuit; synthesis accuracy and available connectivity remain physical costs.

Now let each emitter independently survive with probability $`\eta`$. The no-loss branch multiplies every codeword by $`\sqrt\eta`$. Any loss removes the only excitation and leaves $`|000\rangle`$. Therefore, for every logical density operator $`\rho`$,

```math
\begin{aligned}
\rho\longmapsto{}&
\eta W(\rho\otimes|00\rangle\langle00|)W^\dagger\\
&+(1-\eta)|000\rangle\langle000|.
\end{aligned}
```

At readout, apply $`W^\dagger`$. A surviving state returns to the input qubit with the other emitters in zero, whereas

```math
W^\dagger|000\rangle=|010\rangle.
```

Measuring emitter 2 reveals whether an erasure occurred. On the surviving branch, that measurement does not reveal the logical amplitudes. The receiver retains all flags; failed cells are handled by an outer decoder.

At $`\eta=0.9`$, one cell produces the original qubit with a zero flag with probability $`0.9`$, and a flagged erasure with probability $`0.1`$. Its unassisted erasure-channel capacity is $`0.8`$ qubits per cell, or $`0.8/3`$ per physical emitter. This is a rate over repeated cells, not a promise that every individual cell succeeds.

For example, the [outer stabilizer construction](../science/implementation.md#5-efficient-final-only-stabilizer-recovery) permits a rate of $`0.6`$ logical qubits per cell, hence $`0.2`$ per emitter. With $`m`$ cells, the counted storage is $`3m`$ emitters. Encoding and final syndrome processing have polynomial costs stated there; no syndrome is measured during storage. This construction corrects flagged erasures under its exact channel assumptions. A coherent error on a surviving codeword requires a different argument.

## 4. From the example to an arbitrary dark space

The general model has

```math
L_a=\sum_{j=1}^{B}G_{aj}a_j,\qquad
K_G=\bigcap_{a=1}^{r}\ker L_a.
```

Here a “profile” specifies how one collective mode addresses the emitters. Its rank counts independent spatial directions, not reservoir frequencies. The span is supplied; coefficients mixing modes inside it may be unknown.

The three-emitter example uses only one excitation. The central capacity theorem instead permits the whole dark space, including several excitation sectors. Two facts make that larger choice useful.

First, every local lowering $`a_j`$ commutes with every $`L_a`$. A local-loss jump therefore sends a dark vector to another dark vector. Second, the common kernel splits into orthogonal sectors with a fixed number of excited emitters. The operator counting total excitation is

```math
\widehat N=\sum_j a_j^\dagger a_j.
```

Uniform no-jump attenuation is a function of $`\widehat N`$, so it also preserves the common kernel. Consequently the state stays in a space on which collective dissipation vanishes, even while local loss changes it.

The [model proof](../science/model.md#2-local-loss-preserves-the-whole-dark-space) establishes the resulting channel equality, including reference-entangled inputs:

```math
\Phi_t(\rho)=\mathcal A_\eta^{\otimes B}(\rho),
\qquad
\mathrm{supp}\rho\subseteq K_G.
```

This is a restricted-support statement. The collective and local generators need not commute on arbitrary bright inputs. Homogeneity of the local rate is also essential: unequal attenuation can change relative amplitudes and turn a previously dark vector bright.

## 5. The missing counting step: weight excitations

For the capacity argument below, fix $`1/2\lt \eta\lt 1`$.

The dimension $`\dim K_G`$ is the natural count for noiseless storage. With amplitude damping, the capacity-optimal product input favors an excited-state population $`p_\eta\lt 1/2`$. A useful count must reflect that unequal weighting.

Write $`d_k`$ for the dimension of the dark space in excitation sector $`k`$ and introduce

```math
Z_G(z)=\sum_{k=0}^{B}d_kz^k,
\qquad 0\lt z\lt 1.
```

The weight $`z^k`$ favors lower-excitation sectors. The [weighted-kernel theorem](../science/weighted-kernel.md) proves

```math
Z_G(z)\ge(1+z)^B(1-z)^r.
```

Its short proof has a concrete linear-algebra meaning. Impose the commuting lowering constraints one at a time. The next constraint maps the previously allowed $`k`$-excitation sector into its previously allowed $`(k-1)`$-excitation sector. The number of independent vectors it can remove is at most the target dimension. Weighted summation turns this sectorwise rank-nullity estimate into a factor of at least $`1-z`$ per constraint. Starting with the full-space sum $`(1+z)^B`$ gives the result.

To connect this count to an input state, set

```math
\tau_p=\mathrm{diag}(1-p,p),
\qquad z=\frac{p}{1-p}.
```

The product state is proportional to $`z^{\widehat N}`$. Since the dark projector respects excitation number, the normalized state

```math
\rho_{G,p}=\frac{P_Gz^{\widehat N}}{Z_G(z)}
```

is well defined and supported on $`K_G`$. Its relative entropy from the product input is

```math
\begin{aligned}
D(\rho_{G,p}\Vert\tau_p^{\otimes B})
&=\log_2\frac{(1+z)^B}{Z_G(z)}\\
&\le-r\log_2(1-z).
\end{aligned}
```

This state is a tool for a coding theorem. It describes an average input compatible with the code construction; it is not an instruction to measure an unknown payload and retain only successful projections. No physical postselection is credited with a free rate.

## 6. Why the entropy penalty becomes a capacity penalty

For a product amplitude-damping channel, use the receiver and complementary environment outputs to evaluate

```math
I_c(\rho,\mathcal A_\eta^{\otimes B})
=S(\rho_Y)-S(\rho_E).
```

Write $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$ for binary entropy, with endpoint values defined by continuity. The ordinary one-emitter benchmark is obtained by maximizing

```math
f_\eta(p)=h_2(\eta p)-h_2((1-\eta)p).
```

A tempting shortcut would be to assume that the dark Gibbs input has the same mean excitation as $`\tau_p^{\otimes B}`$. That assumption is unnecessary and generally unjustified.

Instead put $`x=\mathrm{Tr}(\widehat N\rho)-Bp`$. Let $`D_Y`$ and $`D_E`$ denote the output relative entropies from the corresponding product reference states. The [exact entropy identity](../science/capacity.md#3-an-exact-coherent-information-identity) is

```math
I_c
=Bf_\eta(p)+x f_\eta'(p)-D_Y+D_E.
```

This follows by expanding the logarithm of each product reference state. Its logarithm is affine in excitation number, which is why the mismatch appears through one scalar $`x`$.

Choose $`p=p_\eta`$, the capacity optimizer. The derivative vanishes, eliminating the mismatch exactly. Relative-entropy data processing bounds $`D_Y`$ by the input relative entropy, while $`D_E`$ is nonnegative. Thus the weighted estimate supplies

```math
I_c(\rho_{G,p_\eta},\mathcal A_\eta^{\otimes B})
\ge BQ_{\mathrm{AD}}(\eta)-c_\eta r,
```

where

```math
c_\eta=-\log_2(1-z_\eta),\qquad
z_\eta=\frac{p_\eta}{1-p_\eta}.
```

The remaining channel-theoretic step is degradability. For $`\eta\ge1/2`$, a further amplitude-damping channel with survival $`(1-\eta)/\eta`$ reconstructs the environment output from the receiver output. Restricting the original input through an isometry into $`K_G`$ leaves that same degrading map valid. Consequently the restricted channel has a single-letter capacity expression.

Combining these facts gives the [finite capacity theorem](../science/capacity.md#4-a-finite-bound-for-every-profile):

```math
\begin{aligned}
Q_{\mathrm{dark}}(G,\eta)
&\ge\max\{0,BQ_{\mathrm{AD}}(\eta)-c_\eta r\},\\
Q_{\mathrm{dark}}(G,\eta)&\le BQ_{\mathrm{AD}}(\eta).
\end{aligned}
```

The upper bound compares dark-input encodings with unrestricted product amplitude damping. It does not upper-bound every encoding for the full physical dissipator.

The finite penalty is the important refinement. The earlier dimension bound, combined with amplitude-damping thinning, already achieves asymptotic benchmark matching for $`r=o(B)`$. The weighted argument improves the uniform finite cost to order $`r`$ at fixed $`1/2\lt \eta\lt 1`$; the [matching profiles](../science/capacity.md#5-a-matching-family-of-collective-modes) show that this order cannot be improved uniformly.

At zero local loss, the worst dark-dimension penalty instead has order $`r\log(B/r)`$ for $`1\le r=o(B)`$. The constant $`c_\eta`$ diverges as $`\eta`$ approaches one, so these statements have different limits. A smaller penalty relative to a noisy benchmark does not mean that noise increases absolute capacity.

## 7. Four guarantees with different interfaces

| Result | Operational meaning | Required scope |
| --- | --- | --- |
| General dark-input capacity | Near the independent-loss benchmark per emitter when rank is sublinear. | Supplied span, homogeneous local loss, and information-theoretic endpoint coding. |
| Robust common code | One encoder and decoder works for an uncertainty set. | One fixed unknown cell channel, independently repeated, within a certified radius. |
| Constructive erasure route | Explicit positive-rate storage with polynomial outer processing. | Exact flagged-erasure cells; all physical carriers and endpoint operations counted. |
| Robust pair task | Delayed-basis answers outperform any retained classical record. | Static coupling error, quantified added noise and endpoints, and the stated phase reference. |

The [common-code theorem](../science/robustness.md) uses a fixed nominal input, conditional-entropy continuity, and an imported compound-channel theorem. Separate continuity bounds for separately optimized capacities would not supply one decoder that is independent of the unknown channel. The result establishes existence, not an efficient general-purpose decoder.

The [pair task](../science/operational-advantage.md) instead uses the vacuum and a nominal one-excitation dark state as its two logical basis states. Loss can turn logical one into logical zero, so its nominal logical channel is amplitude damping rather than the flagged erasure of the worked three-emitter example. Two emitters are charged per challenge.

That pair calculation explicitly budgets static spatial miscalibration, an arbitrary bright-state phase, additional in-storage dephasing, and endpoint errors. The stated working point has average bit error at most about $`0.08149`$, below the classical retained-record threshold of about $`0.14645`$. Its tolerated-error separation uses the research theorem and independence assumptions cited on the operational page. This finite task certificate is not a demonstration of the near-capacity outer code.

## 8. Calibration and the physical meaning of the bounds

A supplied profile span is information that must come from manufacturing knowledge or calibration. Uncertainty in coefficients inside that span preserves exact darkness. Uncertainty that changes the span can create bright components and needs a channel or generator error budget.

The [calibration account](../science/robustness.md#4-calibration-is-paid-for) separates two kinds of evidence. Fresh BB84 trials can certify the tested procedure's average task error, with an explicitly paid sample and confidence cost. They do not certify the channel's worst-case error on every entangled input. A complete finite-cell channel certificate requires a stronger procedure; the provided conservative tomography cost grows exponentially with cell size.

Confidence also belongs in the final guarantee. A calibration certificate with fixed failure probability does not turn into a certainty merely because a later coding block is long. Its validity must persist through deployment. Testing one convenient pair does not certify a heterogeneous array unless the sampling or physical promise supports that inference.

The ideal collective protection applies during the hold. Fixed endpoint gate counts do not establish accurate gates under unbounded always-on decay; protected boundary windows or certified boundary channels are assumed and charged. Likewise, arbitrary drift of a misaligned bright direction differs from a fixed static error. Unknown vacuum–dark phase, unequal local loss, heating, and cross-cell reservoirs require their stated separate treatment.

Finally, local loss still limits storage time. Positive unassisted dark-input capacity requires $`\eta>1/2`$, or $`\kappa t\lt \ln2`$ when $`\eta=e^{-\kappa t}`$ and $`\kappa>0`$. The achievement is a loss-limited memory whose collective constraints have a controlled capacity cost, together with explicit useful constructions under declared imperfections.

For the complete scientific route, continue from [the model](../science/model.md) through [weighted counting](../science/weighted-kernel.md) and [capacity](../science/capacity.md), then compare [robustness](../science/robustness.md), [implementation](../science/implementation.md), and [the operational task](../science/operational-advantage.md). The [prior-work account](../science/prior-work.md) separates inherited ingredients from the finite rank-dependent refinement.
