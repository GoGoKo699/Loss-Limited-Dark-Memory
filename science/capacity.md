# The capacity cost of collective radiation

[Storage model](model.md) · [Weighted kernel bound](weighted-kernel.md) · [Robustness](robustness.md) · [Implementation](implementation.md) · [Prior work](prior-work.md)

At every fixed nonzero independent-loss level with positive quantum capacity, imposing arbitrary rank-$`r`$ collective dark constraints costs at most a constant times $`r`$ quantum-information bits per cell. A matching family loses one ordinary amplitude-damping channel per collective profile. The resulting worst-profile deficit is linear in $`r`$, whereas the corresponding noiseless dark-space deficit has order $`r\log(B/r)`$.

The theorem is about the dark-input capacity defined in [the model](model.md), not the unrestricted capacity of the full dissipative device. All logarithms and entropies are in bits.

## 1. The independent-loss benchmark

Let

```math
h_2(x)=-x\log x-(1-x)\log(1-x),
\qquad
f_\eta(p)=h_2(\eta p)-h_2((1-\eta)p),
\tag{C1}
```

with entropy values at zero and one defined by continuity. The ordinary amplitude-damping quantum capacity is

```math
Q_{\mathrm{AD}}(\eta)
=\begin{cases}
0,&0\le\eta\le1/2,\\
\displaystyle\max_{0\le p\le1}f_\eta(p),&1/2<\eta\le1.
\end{cases}
\tag{C2}
```

This benchmark and its degradability argument are established results; see [Giovannetti and Fazio (2005)](https://arxiv.org/abs/quant-ph/0405110) and [Wolf and Pérez-García (2007)](https://arxiv.org/abs/quant-ph/0607070). We recall the facts needed for the restricted channel.

A complementary channel of $`\mathcal A_\eta`$ is $`\mathcal A_{1-\eta}`$, up to an environmental basis convention. For $`\eta\ge1/2`$,

```math
\mathcal A_{(1-\eta)/\eta}\circ\mathcal A_\eta
=\mathcal A_{1-\eta}.
\tag{C3}
```

Thus the channel is degradable: its environment output can be reconstructed from its receiver output. For $`\eta\le1/2`$, the reverse relation makes it antidegradable and gives zero unassisted quantum capacity.

For a channel $`\mathcal N`$ with complement $`\mathcal N^c`$, define coherent information by

```math
I_c(\rho,\mathcal N)
=S(\mathcal N(\rho))-S(\mathcal N^c(\rho)).
```

The standard quantum-channel coding theorem expresses capacity as regularized maximum coherent information. Degradability makes that maximum additive and therefore single-letter. One way to see the relevant additivity is to take two degradable channels and an arbitrary joint input. Their coherent information obeys

```math
\begin{aligned}
I_c(\rho_{12},\mathcal N_1\otimes\mathcal N_2)
&=I_c(\rho_1,\mathcal N_1)+I_c(\rho_2,\mathcal N_2)\\
&\quad-I(B_1:B_2)+I(E_1:E_2)\\
&\le I_c(\rho_1,\mathcal N_1)+I_c(\rho_2,\mathcal N_2),
\end{aligned}
\tag{C4}
```

because local degrading maps take $`B_1B_2`$ to $`E_1E_2`$, and mutual information cannot increase under them. Product inputs attain the reverse inequality after maximization.

Coherent information of a degradable channel is concave in the input. Indeed, an isometric extension of a degrading map expresses it as a conditional entropy. Averaging a one-qubit input over phase rotations therefore cannot lower its amplitude-damping coherent information: the channel and complement are phase covariant, and the averaging removes off-diagonal entries. For the resulting diagonal input $`\tau_p=\operatorname{diag}(1-p,p)`$, the receiver and environment excitation probabilities are respectively $`\eta p`$ and $`(1-\eta)p`$. This gives (C1)–(C2).

### The optimizer lies below half excitation

**Lemma 1.** For every $`1/2<\eta<1`$, $`f_\eta`$ has a unique maximizer $`p_\eta\in(0,1/2)`$.

**Proof.** Direct differentiation on $`0<p<1`$ gives

```math
f_\eta''(p)
=-\frac{2\eta-1}
{(\ln2)\,p(1-\eta p)(1-(1-\eta)p)}<0.
\tag{C5}
```

The derivative tends to $`+\infty`$ as $`p\downarrow0`$. To locate its sign at $`p=1/2`$, define

```math
g(\eta)
=\eta\ln\frac{2-\eta}{\eta}
-(1-\eta)\ln\frac{1+\eta}{1-\eta}.
```

Then $`f_\eta'(1/2)=g(\eta)/\ln2`$, while $`g(1/2)=g(1)=0`$ by continuous extension, and

```math
g''(\eta)
=\frac{4(2\eta-1)(\eta^2-\eta+1)}
{\eta(1-\eta)(2-\eta)^2(1+\eta)^2}>0
\quad(1/2<\eta<1).
```

Strict convexity gives $`g(\eta)<0`$ between its two zero endpoints. Thus the strictly decreasing $`f_\eta'`$ has one zero before $`1/2`$, proving the claim. $`\square`$

For the remainder of the positive-capacity theorem put

```math
z_\eta=\frac{p_\eta}{1-p_\eta},
\qquad
c_\eta=-\log(1-z_\eta)
=\log\frac{1-p_\eta}{1-2p_\eta}.
\tag{C6}
```

At fixed $`1/2<\eta<1`$, this is a finite positive constant depending only on the independent-loss level.

## 2. The restricted channel remains degradable

The dark-input channel is

```math
\mathcal N_{G,\eta}
=\mathcal A_\eta^{\otimes B}\circ\mathcal V_G,
\qquad
\mathcal V_G(\rho)=V_G\rho V_G^\dagger.
```

Since $`V_G`$ is an isometry, a complement is

```math
\mathcal N_{G,\eta}^c
=\mathcal A_{1-\eta}^{\otimes B}\circ\mathcal V_G.
```

The product degrading map in (C3) still reconstructs this complement. Consequently

```math
Q_{\mathrm{dark}}(G,\eta)
=\max_{\substack{\rho\ge0,\ \operatorname{Tr}\rho=1\\
                 \operatorname{supp}\rho\subseteq\mathcal K_G}}
I_c(\rho,\mathcal A_\eta^{\otimes B})
\quad(\eta\ge1/2).
\tag{C7}
```

Equation (C7) uses physical input states in the common kernel; it is equivalent to maximizing over the abstract input of $`V_G`$. It follows from the ordinary coding theorem, not from an assumption that one cell realizes its coherent information at finite blocklength. For $`\eta\le1/2`$, the restricted channel is antidegradable as well, and its capacity is zero.

Since a dark-input encoder is also an admissible encoder for ordinary independent amplitude damping,

```math
Q_{\mathrm{dark}}(G,\eta)
\le BQ_{\mathrm{AD}}(\eta).
\tag{C8}
```

This comparison does not constrain unrestricted encodings for the full collective-plus-local generator outside the common kernel.

## 3. An exact coherent-information identity

The following identity avoids converting a sublinear relative-entropy deficit into a weaker trace-distance estimate.

**Lemma 2.** Let $`0<\eta<1`$, $`0<p<1`$, and let $`\rho`$ be any $`B`$-qubit state. Write

```math
\mu=\operatorname{Tr}(\rho\widehat N),\quad
\rho_Y=\mathcal A_\eta^{\otimes B}(\rho),\quad
\rho_E=\mathcal A_{1-\eta}^{\otimes B}(\rho).
```

Then

```math
\begin{aligned}
I_c(\rho,\mathcal A_\eta^{\otimes B})
&=Bf_\eta(p)+(\mu-Bp)f_\eta'(p)\\
&\quad-D(\rho_Y\|\tau_{\eta p}^{\otimes B})
       +D(\rho_E\|\tau_{(1-\eta)p}^{\otimes B}).
\end{aligned}
\tag{C9}
```

**Proof.** For any state $`\sigma`$ and any $`0<q<1`$,

```math
S(\sigma)
=Bh_2(q)+\bigl(\operatorname{Tr}(\sigma\widehat N)-Bq\bigr)
           \log\frac{1-q}{q}
-D(\sigma\|\tau_q^{\otimes B}).
\tag{C10}
```

This follows by expanding $`-\operatorname{Tr}(\sigma\log\tau_q^{\otimes B})`$. Amplitude damping sends mean excitation $`\mu`$ to $`\eta\mu`$, and its complement sends it to $`(1-\eta)\mu`$. Apply (C10) to the two outputs with $`q=\eta p`$ and $`q=(1-\eta)p`$, and subtract. The coefficient of $`\mu-Bp`$ is exactly $`f_\eta'(p)`$. $`\square`$

At the capacity optimizer $`p=p_\eta`$, the mean-excitation correction vanishes exactly. Moreover, relative-entropy data processing gives

```math
D(\rho_Y\|\tau_{\eta p_\eta}^{\otimes B})
\le D(\rho\|\tau_{p_\eta}^{\otimes B}),
```

because the product comparison state is mapped to the indicated product output. Nonnegativity of the environmental relative entropy then implies

```math
I_c(\rho,\mathcal A_\eta^{\otimes B})
\ge BQ_{\mathrm{AD}}(\eta)
-D(\rho\|\tau_{p_\eta}^{\otimes B}).
\tag{C11}
```

No assumption about the actual mean excitation of $`\rho`$ is needed in (C11).

## 4. A finite bound for every profile

**Theorem 3 — Finite capacity penalty.** For every rank-$`r`$ profile matrix $`G\in\mathbb C^{r\times B}`$ and fixed $`1/2<\eta<1`$,

```math
\max\{0,\,BQ_{\mathrm{AD}}(\eta)-c_\eta r\}
\le Q_{\mathrm{dark}}(G,\eta)
\le BQ_{\mathrm{AD}}(\eta).
\tag{C12}
```

**Proof.** Use the dark Gibbs state $`\rho_{G,p_\eta}`$ from [the weighted bound](weighted-kernel.md). Its relative entropy from the optimal product input is at most $`c_\eta r`$. Equation (C11), followed by the maximization in (C7), proves the lower bound. Capacity is nonnegative, and (C8) supplies the upper bound. $`\square`$

Every cell has $`B`$ physical carriers, including all initialized redundancy. Equation (C12) is uniform over arbitrary inhomogeneous profile coefficients and independent of the finite collective rates in the exact model.

As an immediate consequence, for any sequence $`r_B=o(B)`$,

```math
\sup_{\operatorname{rank}G=r_B}
\left|
\frac{Q_{\mathrm{dark}}(G,\eta)}B-Q_{\mathrm{AD}}(\eta)
\right|
\le c_\eta\frac{r_B}{B}\longrightarrow0.
\tag{C13}
```

Thus collective radiation imposes asymptotically no rate penalty relative to the independent-loss benchmark within the dark-input architecture. This is a capacity statement, with the coding convention specified in the model.

The qualitative limit also follows from the inherited unweighted dimension deficit. To make that comparison explicit, put $`d_G=\dim\mathcal K_G`$ and define

```math
\widetilde\rho_G
=\mathcal A_{2p_\eta}^{\otimes B}(P_G/d_G).
```

This is a valid dark-supported state because $`0<2p_\eta<1`$ and homogeneous amplitude damping preserves the common kernel. The same attenuation maps $`(I/2)^{\otimes B}`$ to $`\tau_{p_\eta}^{\otimes B}`$. Consequently data processing gives

```math
D(\widetilde\rho_G\|\tau_{p_\eta}^{\otimes B})
\le D(P_G/d_G\|(I/2)^{\otimes B})
=B-\log d_G.
```

Equation (C11) therefore already implies the finite earlier baseline

```math
Q_{\mathrm{dark}}(G,\eta)
\ge \max\{0,\;BQ_{\mathrm{AD}}(\eta)-(B-\log d_G)\}.
```

The inherited dimension bound makes this deficit at most $`\log\binom{B+r}{r}`$, which is sublinear whenever $`r=o(B)`$. Thus the qualitative limit (C13) does not depend on the weighted refinement. The refinement supplies the stronger finite conclusion in (C12): a loss of at most $`c_\eta`$ information bits per profile, in place of the worst-case logarithmic dimension overhead. As with the weighted input, the attenuated state is an input distribution used by the coding theorem, not a prescription to damp an unknown payload before storage.

## 5. A matching family of collective modes

Define the worst-profile deficit by

```math
\Delta_{\max}(B,r;\eta)
=BQ_{\mathrm{AD}}(\eta)
-\inf_{\substack{G\in\mathbb C^{r\times B}\\\operatorname{rank}G=r}}
 Q_{\mathrm{dark}}(G,\eta).
\tag{C14}
```

The infimum avoids any unnecessary continuity assumption about kernel dimension as profiles change. The finite upper bound in (C12) gives

```math
\Delta_{\max}(B,r;\eta)
\le\min\{BQ_{\mathrm{AD}}(\eta),c_\eta r\}.
\tag{C15}
```

**Proposition 4 — Disjoint collective-pair example.** If $`B\ge2r`$, there are rank-$`r`$ collective profiles for which

```math
Q_{\mathrm{dark}}(G,\eta)=(B-r)Q_{\mathrm{AD}}(\eta).
\tag{C16}
```

**Proof.** For $`a=1,\ldots,r`$, use the disjoint profiles

```math
L_a=a_{2a-1}+a_{2a}.
```

On each pair the kernel is exactly

```math
\mathcal K_{\mathrm{pair}}
=\operatorname{span}\{|00\rangle,|s\rangle\},
\qquad
|s\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}.
```

Under independent local amplitude damping,

```math
\begin{aligned}
|00\rangle\langle00|&\longmapsto|00\rangle\langle00|,\\
|s\rangle\langle s|&\longmapsto
\eta|s\rangle\langle s|+(1-\eta)|00\rangle\langle00|,\\
|00\rangle\langle s|&\longmapsto
\sqrt\eta\,|00\rangle\langle s|.
\end{aligned}
\tag{C17}
```

These four matrix-unit actions, including the adjoint of the last, identify exactly one logical channel $`\mathcal A_\eta`$ on the pair. The other $`B-2r`$ emitters are unrestricted and each contributes another $`\mathcal A_\eta`$. The full restricted channel is therefore unitarily equivalent, on its input and supported output, to $`\mathcal A_\eta^{\otimes(B-r)}`$. Its capacity is (C16). $`\square`$

The profile class explicitly permits the zero coefficients outside these disjoint pairs. No emitters are omitted from the resource denominator. The pair encoding is standard subradiant physics; here it supplies a matching example for a uniform rank law, rather than a separate new protection mechanism.

For all $`r\le B`$, an alternative admissible example uses $`r`$ independent single-site lowering profiles. Its common kernel fixes those $`r`$ emitters in their ground states and again gives (C16). This extends the lower deficit bound to the whole rank range.

**Corollary 5 — Sharp noisy rank order.** For every $`1\le r\le B`$ and fixed $`1/2<\eta<1`$,

```math
rQ_{\mathrm{AD}}(\eta)
\le\Delta_{\max}(B,r;\eta)
\le\min\{BQ_{\mathrm{AD}}(\eta),c_\eta r\}.
\tag{C18}
```

In particular,

```math
\Delta_{\max}(B,r;\eta)=\Theta_\eta(r).
\tag{C19}
```

The constants depend on the fixed local-loss parameter. The result matches the order, not the optimal coefficient or exact finite worst-profile capacity. For the sublinear-rank regime, the two-emitter collective example already supplies the lower bound for all sufficiently large cells.

## 6. Endpoints and the nonuniform zero-loss limit

The three regimes should be kept separate.

| Local survival | Dark-input capacity and worst-profile statement |
| --- | --- |
| $`0\le\eta\le1/2`$ | Every restricted channel is antidegradable; $`Q_{\mathrm{dark}}=0`$. |
| Fixed $`1/2<\eta<1`$ | Equations (C12) and (C18) give the finite linear-rank penalty. |
| $`\eta=1`$ | The restricted channel is noiseless on $`\mathcal K_G`$; $`Q_{\mathrm{dark}}(G,1)=\log\dim\mathcal K_G`$. |

At the noiseless endpoint, the inherited dimension law in [the weighted-kernel account](weighted-kernel.md#4-relation-to-the-noiseless-dimension-law) gives

```math
\Delta_{\max}(B,r;1)
=\Theta\!\left(r\log\frac Br\right),
\qquad1\le r=o(B).
\tag{C20}
```

This is the same deficit definition as (C14), since $`Q_{\mathrm{AD}}(1)=1`$. The laws compare the additional restriction imposed by collective darkness against the independent-loss benchmark appropriate to each noise level.

There is no contradiction with finite-dimensional continuity. As $`\eta\to1`$, the unique maximizing populations tend to $`1/2`$: the continuous objectives $`f_\eta`$ approach $`h_2`$, whose maximizer is unique. Consequently $`z_\eta\to1`$ and $`c_\eta\to\infty`$. The linear-rank bound is not uniform in the zero-loss limit. For a fixed profile and finite cell, its capacity can approach the noiseless value continuously while the large-cell asymptotic form changes.

The worst profiles in the two regimes need not be identical. Nor does a smaller relative penalty mean that adding noise increases absolute capacity. It means that, when local loss is already unavoidable, the capacity-relevant low-excitation input pays a different cost for the collective constraints than a maximally mixed noiseless input does.

## 7. From a capacity law to a usable memory

The exact theorem establishes an information-theoretic endpoint: with no intervention during storage, one can approach the local-loss benchmark while paying the stated rank-dependent rate loss. The capacity theorem does not itself provide a polynomial-time compiler or decoder near that benchmark.

[Implementation](implementation.md) gives separate explicit lower-rate constructions and resource accounting. [Robustness](robustness.md) shows how a fixed uncertainty neighborhood of a finite cell yields a common code when calibration is imperfect and extra noise is present. That extension preserves a positive achievable rate under its stated uncertainty model; it does not assert equality with $`Q_{\mathrm{AD}}`$ after arbitrary perturbations. The [operational task](operational-advantage.md) makes the comparison with classical retention explicit.

The ingredients have distinct ownership. Ordinary amplitude-damping capacity, degradable-channel coding, and collective dark states are established. The earlier arbitrary-profile memory supplies the unweighted nilpotent dimension argument. The contribution proved here is its weighted refinement, the exact local-loss reduction on the full dark space, and their finite $`O(r)`$ capacity penalty with matching worst-profile order. The [prior-work comparison](prior-work.md) states the surrounding literature and remaining implementation boundaries.
