# A weighted bound for collective dark spaces

[Storage model](model.md) · [Capacity theorem](capacity.md) · [Prior work](prior-work.md)

Counting dark vectors is sufficient for noiseless storage. With independent amplitude damping, the capacity-optimal input favors lower excitation. The relevant counting object is therefore a weighted dimension. This page proves a bound uniform over arbitrary supplied collective lowering profiles and converts it into a relative-entropy estimate.

All logarithms are base two. Let $`G\in\mathbb C^{r\times B}`$ have row rank $`r`$, and retain the operators $`L_a`$, common kernel $`\mathcal K_G`$, and excitation number $`\widehat N`$ from [the model](model.md). Write

**(W1)**

```math
\mathcal H_k=\ker(\widehat N-kI),\qquad
d_k=\dim(\mathcal K_G\cap\mathcal H_k),\qquad
Z_G(z)=\mathrm{Tr}(P_Gz^{\widehat N})
=\sum_{k=0}^{B}d_kz^k.
```

## 1. Weighted common-kernel theorem

**Theorem 1.** For every $`0\lt z\lt 1`$,

**(W2)**

```math
Z_G(z)\ge(1+z)^B(1-z)^r.
```

The statement is independent of coefficient magnitudes, phases, and spacing. It also holds when $`r`$ is merely the number of supplied profiles, but replacing that number by their actual rank gives the stronger bound. For $`r=0`$, equality holds.

### Proof

The lowering operators commute and have bounded total degree:

**(W3)**

```math
[L_a,L_b]=0,\qquad
L^\alpha:=L_1^{\alpha_1}\cdots L_r^{\alpha_r}=0
\quad\text{when }|\alpha|>B.
```

Indeed, products of more than $`B`$ individual lowering operators repeat a site, and $`a_j^2=0`$.

For a fixed excitation sector, consider the linear map

**(W4)**

```math
T_k:\mathcal H_k\longrightarrow
\bigoplus_{\substack{\alpha\in\mathbb N_0^r\\|\alpha|\le k}}
\mathcal K_{G,k-|\alpha|},
\qquad
T_k\psi=(P_GL^\alpha\psi)_\alpha.
```

The target grading follows from Lemma 1 of [the model](model.md): $`P_G`$ preserves excitation sectors, and $`L^\alpha`$ lowers excitation by $`|\alpha|`$.

The map $`T_k`$ is injective. Given $`\psi\ne0`$, choose a multi-index $`\alpha`$ of maximal total degree for which $`L^\alpha\psi\ne0`$. The zero multi-index is available, and every nonzero monomial has degree at most $`k`$. Commutation and maximality imply

```math
L_aL^\alpha\psi=0
\quad\text{for every }a.
```

Thus $`L^\alpha\psi`$ already lies in $`\mathcal K_{G,k-|\alpha|}`$, and its projection by $`P_G`$ is nonzero. At least one component of $`T_k\psi`$ is therefore nonzero. Comparing dimensions gives

**(W5)**

```math
\binom Bk
\le
\sum_{\substack{\alpha\in\mathbb N_0^r\\|\alpha|\le k}}
d_{k-|\alpha|}.
```

Multiply (W5) by $`z^k`$ and sum over $`k`$. Reindex with $`j=k-|\alpha|`$:

**(W6)**

```math
\begin{aligned}
(1+z)^B
&\le
\sum_{j=0}^{B}d_jz^j
\sum_{\substack{\alpha\in\mathbb N_0^r\\|\alpha|\le B-j}}
z^{|\alpha|}\\
&\le
Z_G(z)\sum_{\alpha\in\mathbb N_0^r}z^{|\alpha|}\\
&=Z_G(z)(1-z)^{-r}.
\end{aligned}
```

The last series converges because $`z\lt 1`$. Rearranging proves (W2). For $`r=0`$, the only multi-index is empty and every map is the identity. $`\square`$

The proof is a graded refinement of the nilpotent injection in [Multimode Dark Memory](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/rank-law.md). The injection is inherited; the weighted partition-function consequence is what is needed for the noisy capacity bound. Constructing all components of $`T_k`$ is not assumed to be an efficient encoder.

### A second proof by successive kernel constraints

There is also a short rank-nullity proof. Let

```math
\mathcal K^{(a)}=\bigcap_{j=1}^{a}\ker L_j,\qquad
h_k^{(a)}=\dim(\mathcal K^{(a)}\cap\mathcal H_k),\qquad
Z_a(z)=\sum_{k=0}^{B}h_k^{(a)}z^k,
```

starting with the full space at $`a=0`$. Commutation implies that $`L_a`$ maps $`\mathcal K^{(a-1)}\cap\mathcal H_k`$ into $`\mathcal K^{(a-1)}\cap\mathcal H_{k-1}`$. Rank-nullity therefore gives

```math
h_k^{(a)}
\ge h_k^{(a-1)}-h_{k-1}^{(a-1)},
\qquad h_{-1}^{(a-1)}=0.
```

The right side may be negative, which does not invalidate the lower bound. Multiplying by the positive weights and summing yields

```math
Z_a(z)
\ge(1-z)Z_{a-1}(z)+z^{B+1}h_B^{(a-1)}
\ge(1-z)Z_{a-1}(z).
```

Since $`1-z>0`$, iteration is valid and gives $`Z_r(z)\ge(1-z)^rZ_0(z)=(1-z)^r(1+z)^B`$. This independently proves (W2), using only the commuting degree-lowering structure.

## 2. A dark input close in relative entropy to a product input

For $`0\lt p\lt 1/2`$, define

```math
\tau_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|,
\qquad
z=\frac p{1-p}\in(0,1).
```

The corresponding product state is

```math
\tau_p^{\otimes B}=\frac{z^{\widehat N}}{(1+z)^B}.
```

Since $`P_G`$ commutes with $`\widehat N`$, conditioning this product state on the dark subspace gives a legitimate density operator

**(W7)**

```math
\rho_{G,p}
=\frac{P_Gz^{\widehat N}}{Z_G(z)}.
```

This is a mathematical input state for the channel-coding bound. It is not a requirement that an unknown stored payload be replaced by a mixed state, nor a proposal to implement the encoder by postselecting a physical projection.

**Corollary 2.** With relative entropy measured in bits,

**(W8)**

```math
\begin{aligned}
D\!\left(\rho_{G,p}\middle\|\tau_p^{\otimes B}\right)
&=\log\frac{(1+z)^B}{Z_G(z)}\\
&\le-r\log(1-z)\\
&=r\log\frac{1-p}{1-2p}.
\end{aligned}
```

**Proof.** On the support of $`\rho_{G,p}`$,

```math
\log\rho_{G,p}
=(\log z)\widehat N-\log Z_G(z),
\qquad
\log\tau_p^{\otimes B}
=(\log z)\widehat N-B\log(1+z).
```

Their difference is a scalar there. Taking its expectation proves the equality in (W8), and Theorem 1 gives the bound. The comparison state is full rank, so the relative entropy is finite. $`\square`$

Equivalently, the product state has dark-space weight

```math
w_G(p)=\mathrm{Tr}(P_G\tau_p^{\otimes B})
\ge(1-z)^r,
```

and the conditioning costs at most $`-\log w_G(p)`$ information bits. At fixed $`p\lt 1/2`$, this cost is linear in the number of profiles and independent of the number of emitters per profile.

## 3. Why the excitation weight matters

The factor in (W2) has a simple sharpness check. For one uniform collective lowering operator on $`B`$ emitters, the familiar spin decomposition gives

**(W9)**

```math
d_k=\binom Bk-\binom B{k-1}
\quad(0\le k\le\lfloor B/2\rfloor),
\qquad d_k=0\quad(k>\lfloor B/2\rfloor),
```

where $`\binom B{-1}=0`$. Put $`m=\lfloor B/2\rfloor`$ and let $`X\sim\mathrm{Bin}(B,p)`$, with $`p=z/(1+z)\lt 1/2`$. Then

**(W10)**

```math
\frac{Z_G(z)}{(1+z)^B}
=\Pr(X\le m)-z\Pr(X\le m-1)
\longrightarrow1-z.
```

Both probabilities tend to one because the mean lies strictly below $`B/2`$. Thus the one-profile factor $`1-z`$ is attained asymptotically at the partition-function level. Disjoint large uniform groups give the corresponding product factor for any fixed number of groups. This does not by itself determine the exact capacity deficit of those groups.

The distinction from the unweighted count is useful: an amplitude-damping-optimal product input has $`p\lt 1/2`$ at every fixed nonzero loss below the antidegradability threshold. It places its typical weight below the half-excitation boundary. The dark-space restriction then removes a bounded amount of relative-entropy weight per collective profile.

## 4. Relation to the noiseless dimension law

Keeping the finite monomial sum in (W6), rather than replacing it by an infinite geometric series, permits $`z=1`$. There are $`\binom{B+r}{r}`$ multi-indices of degree at most $`B`$. Hence the inherited unweighted bound is

**(W11)**

```math
\dim\mathcal K_G
\ge\frac{2^B}{\binom{B+r}{r}}.
```

Its worst-profile dimension redundancy has order

**(W12)**

```math
B-\log\min_{\mathrm{rank}G=r}\dim\mathcal K_G
=\Theta\!\left(r\log\frac Br\right),
\qquad1\le r=o(B).
```

For completeness, the two directions use the same admissible profile class as (M1). Equation (W11) and the standard binomial bound give the upper redundancy bound

```math
B-\log\dim\mathcal K_G
\le r\log\frac{e(B+r)}r.
```

For the other direction, divide the emitters into $`r`$ groups of sizes $`b_a=B/r+O(1)`$ and assign one uniform lowering profile to each group. The common dark space factorizes, and the established single-mode count gives

```math
\dim\mathcal K_G
=\prod_{a=1}^{r}\binom{b_a}{\lfloor b_a/2\rfloor}.
```

Since

```math
\log\binom b{\lfloor b/2\rfloor}
=b-\tfrac12\log b+O(1),
```

the redundancy of this example is at least $`\tfrac r2\log(B/r)-O(r)`$. This proves the order in (W12), while leaving the optimal leading constant open.

The single-mode dark count is established collective-decay coding; see [Duan and Guo (1998)](https://arxiv.org/abs/quant-ph/9804014). The arbitrary-profile bound and worst-profile dimension order are inherited from the pinned [Multimode Dark Memory account](https://github.com/GoGoKo699/Multimode-Dark-Memory/blob/f7ef50082452c7b29c66322ca51e9cf6b0f5b1eb/science/rank-law.md). The new noisy [capacity law](capacity.md) uses (W8) to replace this logarithmic-per-profile overhead by a constant-per-profile information penalty at fixed loss.
