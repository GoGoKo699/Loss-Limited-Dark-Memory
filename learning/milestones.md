# Thirty milestones for loss-limited dark memory

[Scientific map](../science/README.md) · [Wilde bridge](wilde-bridge.md) · [Reference index](../references/README.md)

The scientific question is how much useful quantum information remains when collective radiation can be avoided, independent local loss cannot, and the device description is imperfect. The answer connects three kinds of statement: a capacity law for arbitrary collective profiles, a common-code guarantee under channel uncertainty, and explicit constructions with charged endpoints and classical comparators.

The single educational anchor is **Mark M. Wilde, *From Classical to Quantum Shannon Theory*, [arXiv:1106.1445v8 (2019)][wilde]**, the public draft associated with *Quantum Information Theory*, second edition (2017). Section numbers below refer to that arXiv version. The [bridge](wilde-bridge.md) translates its channel and information notation into this project's emitter model. The anchor supplies the quantum-information framework; the project pages supply the lowering-operator algebra, the weighted rank argument, and the particular robustness and retrieval constructions. Research theorems imported by those pages retain their primary-source attribution.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The first phase builds from a single stored qubit to an operationally defined noisy memory. The second builds from local dark-space invariance to the rank-capacity theorem, then incorporates uncertainty, implementation, and a finite quantum advantage. This allocation gives the algebraic proof and the operational consequences separate space without treating the textbook's contents as the project's story. The map identifies the connected understanding targets; specialist calculations remain in the linked scientific sources.

## Phase I — Background and preliminaries: from a state to a memory channel

### M01. States and retained coherence

**Central question.** What must a memory retain when its input is an unknown quantum state?

**Understanding target.** A qubit is a state in a two-dimensional logical space, not just an unknown classical bit. Its populations and relative phase jointly determine later measurement outcomes; an incoherent mixture with the same populations need not give the same answers. A density operator describes both pure states and mixtures, while an encoding places the same logical information in a larger physical system.

**Dependencies and story role.** This is the local starting point. It gives meaning to storing the vacuum and a one-excitation dark state as a logical qubit, before any claim about a long memory or a large code.

**Conceptual connection.** Delayed-basis retrieval requires coherence to survive until the basis is revealed. Preserving excitation probability alone therefore cannot establish the task advantage.

**Source pointers.** [Wilde v8][wilde], §§3.2–3.4 and 4.1; [Operational advantage](../science/operational-advantage.md), §§1–2 and (O1)–(O4).

### M02. Composite systems and an inaccessible reference

**Central question.** Why is preserving a state entangled with another system the relevant standard for quantum storage?

**Understanding target.** Tensor products describe the physical emitters, but their joint state need not factorize. A memory must preserve correlations with an inaccessible reference, not merely reproduce a few unentangled inputs. Tracing out an auxiliary system describes discarding it, and a reference used to assess fidelity supplies no assistance to the memory.

**Dependencies and story role.** M01 supplies the single-system state. This milestone extends the object being preserved to a joint state and makes the distinction between device carriers and verifier resources explicit.

**Conceptual connection.** The same reference system appears in coherent information, diamond-distance guarantees, and the Bell-pair storage witness. Counting all device-accessible carriers during the hold prevents a protected auxiliary register from supplying an uncharged quantum memory.

**Source pointers.** [Wilde v8][wilde], §§3.5–3.6, 4.3, and 5.1; [Model](../science/model.md), §4; [Implementation](../science/implementation.md), §§1 and 6.

### M03. Channels, Kraus branches, and the environment

**Central question.** How can one describe noisy evolution without keeping the environment as part of the accessible memory?

**Understanding target.** A completely positive trace-preserving channel acts consistently on states, including inputs entangled with a reference. Kraus operators describe branches whose probabilities sum to one. An isometric dilation assigns both a receiver output and a complementary environment output, making information leakage a property of the channel rather than an informal picture of decay.

**Dependencies and story role.** M01–M02 provide states and composite systems. Channel composition now connects encoding, the passive hold, and decoding into one operational map.

**Conceptual connection.** Local-loss jumps and no-jump evolution will be analyzed separately to prove dark-space invariance. The environment output will later enter the coherent-information capacity calculation.

**Source pointers.** [Wilde v8][wilde], §§4.4–4.5 and 5.2; [Model](../science/model.md), (M4), (M6), and Proposition 3; [Capacity](../science/capacity.md), §§1–2.

### M04. One emitter under amplitude damping

**Central question.** Which parts of a qubit state change when an excitation can be lost?

**Understanding target.** The channel $`\mathcal A_\eta`$ has excited-state survival $`\eta`$, so an excited-state population is multiplied by $`\eta`$ while ground-to-excited coherence is multiplied by $`\sqrt\eta`$. A decay branch ends in the ground state; the no-decay branch also changes superpositions. In this project $`\eta=e^{-\kappa t}`$ is survival, not loss probability.

**Dependencies and story role.** M03 supplies the channel and Kraus description. This milestone gives the local noise process that remains after collective protection is imposed.

**Conceptual connection.** A dark code can remove one physical decay mechanism while still undergoing this channel. Its meaningful benchmark is therefore the capacity of ordinary local damping at the same $`\eta`$, with the same physical-carrier accounting.

**Source pointers.** [Wilde v8][wilde], §§4.7 and 24.7.2; [Model](../science/model.md), (M2)–(M4); [Capacity](../science/capacity.md), §1.

### M05. Collective lowering, kernels, and excitation grading

**Central question.** How can several emitters contain a state that a collective emission mode cannot lower?

**Understanding target.** A collective jump is a linear combination $`L=\sum_jg_ja_j`$ of one-site lowering operators. Its kernel contains states whose emission amplitudes cancel. The vacuum and the antisymmetric one-excitation state of a uniform pair illustrate the distinction between a protected subspace and an individual physical emitter. Lowering reduces total excitation by one, so excitation sectors organize both the kernel and its dimension.

**Dependencies and story role.** M02–M04 provide composite systems and decay channels. This milestone introduces the finite-dimensional linear algebra needed to discuss many collective constraints.

**Conceptual connection.** Commuting lowering operators, excitation grading, and eventual annihilation under repeated lowering will make the later rank argument possible. Wilde supplies the channel interpretation; the particular lowering algebra is supplied by the project.

**Source pointers.** [Wilde v8][wilde], §§4.4–4.7; [Model](../science/model.md), §§1–2 and Lemma 1; [Weighted kernel](../science/weighted-kernel.md), (W1)–(W4).

### M06. Entropy and coherent information

**Central question.** Which information quantity distinguishes a quantum output from information leaked to its environment?

**Understanding target.** Quantum entropy depends on the eigenvalues of a state. For a purified channel input, coherent information can be written as receiver entropy minus environment entropy, or as minus the reference's conditional entropy given the receiver. A positive value measures an asymmetry useful for transmitting entanglement; it is not merely the output's excitation count or classical uncertainty.

**Dependencies and story role.** M02–M03 provide the reference and complementary output. This milestone turns physical decay into an information comparison.

**Conceptual connection.** The project's capacity proof must control both outputs of amplitude damping. A large dark-space dimension alone does not determine their entropy difference after local noise.

**Source pointers.** [Wilde v8][wilde], §§11.1, 11.4–11.5, and 13.5; [Capacity](../science/capacity.md), §§1 and 3.

### M07. Relative entropy and comparison states

**Central question.** How can a complicated dark-supported state be compared with a simple product input without requiring small trace distance?

**Understanding target.** Relative entropy $`D(\rho\|\sigma)`$ quantifies a state comparison with a specified reference state and is finite when the relevant support is contained in that reference's support. It cannot increase when the same channel acts on both states. For a product Bernoulli reference $`\tau_p^{\otimes B}`$, the logarithm of the reference is an affine function of total excitation, which makes entropy expansions tractable.

**Dependencies and story role.** M04 and M06 supply the damping channel and entropy. This milestone introduces the comparison method that will connect a weighted dimension bound to coherent information.

**Conceptual connection.** A bound of order $`r`$ on relative entropy can be useful even when it is not a small absolute error. The proof will use data processing directly instead of weakening that information through an unnecessary trace-distance conversion.

**Source pointers.** [Wilde v8][wilde], §11.8; [Weighted kernel](../science/weighted-kernel.md), §2; [Capacity](../science/capacity.md), Lemma 2 and (C10)–(C11).

### M08. Degradability and the receiver–environment ordering

**Central question.** When does the environment's output contain no more information than can be reconstructed from the receiver's output?

**Understanding target.** A degradable channel admits a channel from the receiver output to the complementary output. For amplitude damping, survival parameters compose multiplicatively, giving a degrading map when $`\eta\ge1/2`$. Below that threshold the reverse ordering makes the channel antidegradable. Degradability supports a single-letter coherent-information capacity formula; antidegradability precludes positive unassisted quantum capacity.

**Dependencies and story role.** M03–M04 and M06 supply complementary channels, their compositions, and coherent information. This milestone identifies the special channel structure that makes an exact capacity comparison possible.

**Conceptual connection.** Precomposing with an isometric restriction to a dark input space preserves the same degrading relation. That fact will justify an actual restricted-channel capacity statement, not just a lower bound on one input's coherent information.

**Source pointers.** [Wilde v8][wilde], §13.5 and §§24.7.1–24.7.2; [Capacity](../science/capacity.md), (C3)–(C4) and §2.

### M09. Capacity as a repeated-use operational limit

**Central question.** What does a rate of logical qubits per physical emitter assert about a family of memories?

**Understanding target.** Quantum capacity is defined through encoders and decoders over many channel uses with fidelity tending to one. It is not the fidelity of one cell or the logarithm of a convenient code space after noise. A cell contains $`B`$ counted emitters, so $`m`$ uses consume $`mB`$ carriers and a payload of $`k`$ qubits has physical rate $`k/(mB)`$. Coding existence and efficient boundary circuits are different resource statements.

**Dependencies and story role.** M02, M06, and M08 connect entanglement preservation, information quantities, and the channel class. This milestone gives those quantities their global communication meaning.

**Conceptual connection.** The project first takes the coding limit over repeated finite cells. A later limit with $`r/B\to0`$ compares cell capacities; it does not silently replace that coding limit by one uncoded growing cell.

**Source pointers.** [Wilde v8][wilde], chapter 24 and §9.5; [Model](../science/model.md), §4; [Capacity](../science/capacity.md), §§2 and 7.

### M10. The optimal input for a lossy qubit

**Central question.** Why is the capacity-optimal input of a locally damped qubit biased toward the ground state?

**Understanding target.** Phase covariance and concavity permit an optimal diagonal input with excited population $`p`$. Its coherent information is $`f_\eta(p)=h_2(\eta p)-h_2((1-\eta)p)`$. At every fixed $`1/2<\eta<1`$, the project proves a unique optimizer $`p_\eta\in(0,1/2)`$ with $`f_\eta'(p_\eta)=0`$. The noiseless maximally mixed input is therefore not the appropriate finite-loss reference.

**Dependencies and story role.** M04 and M06–M09 supply damping, entropy, degradability, and capacity. This milestone locates the population around which the dark-space comparison must be organized.

**Conceptual connection.** The strict inequality $`p_\eta<1/2`$ makes the excitation weight $`z_\eta=p_\eta/(1-p_\eta)`$ less than one. Stationarity at $`p_\eta`$ will cancel a mean-excitation correction in the main proof.

**Source pointers.** [Wilde v8][wilde], §24.7.2; [Capacity](../science/capacity.md), §1, Lemma 1, and (C5)–(C6).

### M11. Flagged erasure and unflagged damping

**Central question.** Why does knowing where a loss occurred change the decoding problem?

**Understanding target.** An erasure channel sends the input through intact or replaces it by an orthogonal flag. Amplitude damping generally leaves no such logical flag and also distorts no-jump superpositions. A $`d`$-level erasure channel with survival $`\eta`$ has unassisted capacity $`\max\{0,2\eta-1\}\log_2d`$. Its flag is available at retrieval; it does not supply a second opportunity to encode the original unknown input during storage.

**Dependencies and story role.** M03–M04 and M08–M09 supply channel structure and the capacity interface. This milestone compares two residual-noise channels before they reappear as different constructions in the project.

**Conceptual connection.** Confining a cell to one excitation can make vacuum an orthogonal erasure flag. That simplification enables efficient recovery, while using only a smaller part of the many-excitation dark space.

**Source pointers.** [Wilde v8][wilde], §§24.7.1–24.7.2; [Implementation](../science/implementation.md), §§3 and 5; [Capacity](../science/capacity.md), §7.

### M12. An operational framework for a noisy memory

**Central question.** Which ingredients must be specified before a passive-memory advantage is a meaningful claim?

**Understanding target.** A memory statement combines an input interface, a physical hold channel, boundary operations, a reliability criterion, and counted resources. Trace distance controls differences in measurement probabilities; a diamond-distance bound extends this protection to reference-entangled inputs. A nominal capacity law, a uniform uncertainty guarantee, and a finite retrieval score answer different questions and require compatible assumptions about repeated cells and endpoint error.

**Dependencies and story role.** M01–M11 now form one framework: states and references identify what is preserved, channels identify the noise, and coding gives rates and reliability. This closes the background phase by assembling those local objects into a complete operational statement.

**Conceptual connection.** The subsequent narrative uses this framework to separate the full dark-input capacity theorem from the simpler erasure code and pair witness. Passive refers to the hold interval; preparation, retrieval, and calibration remain physical resources.

**Source pointers.** [Wilde v8][wilde], §§9.1–9.2, §9.5, and chapter 24; [Model](../science/model.md), §§4–5; [Robustness](../science/robustness.md), §§1 and 5; [Scientific map](../science/README.md).

## Phase II — Narrative and innovation: from dark invariance to a usable advantage

### M13. The supplied profile span defines the architecture

**Central question.** What exactly is removed by restricting inputs to the common dark space?

**Understanding target.** The rank-$`r`$ matrix $`G`$ specifies collective lowering operators $`L_a=\sum_jG_{aj}a_j`$ and their common kernel $`\mathcal K_G`$. Row rank counts independent constraints, regardless of how many redundant modes are listed. Arbitrary coefficients are allowed in the supplied span. The capacity under study restricts inputs to this kernel and counts every one of the $`B`$ emitters; it does not optimize all bright-sector encodings for the full physical channel.

**Dependencies and story role.** M05 and M12 supply dark kernels and the operational interface. The narrative begins by fixing the physical object and the precise architecture whose capacity will be compared.

**Conceptual connection.** A change of basis among supplied profiles changes their representation but not their common kernel. This distinction between a span and its coordinates later determines which calibration uncertainties are harmless exactly.

**Source pointers.** [Wilde v8][wilde], §§4.4–4.7 and chapter 24 for channel restrictions and operational rates; [Model](../science/model.md), §§1 and 4, (M1)–(M2), and (M8).

### M14. Local loss stays inside the dark space

**Central question.** Why does an independent decay event not necessarily activate the collective loss that the code avoided?

**Understanding target.** Each local lowering operator commutes with every collective lowering operator, so a local jump maps a common dark vector to another common dark vector. Excitation grading makes the uniform no-jump factor, a function of $`\widehat N`$, preserve the same space. Every product Kraus branch of homogeneous local damping therefore stays dark, and the simultaneous collective-plus-local evolution equals ordinary product amplitude damping on dark inputs.

**Dependencies and story role.** M03–M05 and M13 provide Kraus branches, the excitation grading, and the physical model. This is the physical reduction on which the rest of the argument depends.

**Conceptual connection.** The proof concerns an invariant input space; it does not require the full collective and local generators to commute. Homogeneity of the local no-jump evolution is load bearing, and generic nonuniform damping is not included by this reasoning.

**Source pointers.** [Wilde v8][wilde], §§4.4–4.5 and §24.7.2; [Model](../science/model.md), Lemmas 1–2, Proposition 3, and (M5)–(M7).

### M15. The graded injection behind the rank proof

**Central question.** How can arbitrary inhomogeneous lowering profiles still force a large common kernel?

**Understanding target.** In a fixed excitation sector, the map taking a vector to all projected lowering descendants is injective. For any nonzero vector, choose a nonzero descendant of maximal lowering degree. Commutation and maximality make it dark, so at least one projected descendant is nonzero. Comparing source and target dimensions produces a sector inequality involving the dark dimensions at lower excitations.

**Dependencies and story role.** M05 and M13–M14 provide commuting lowerings and the excitation sectors. This is the local algebraic step before summing information across all sectors.

**Conceptual connection.** Nilpotence supplies a terminating descent, while projection into the common kernel records its surviving endpoint. This explains why the bound is uniform over coefficient values. The inherited injection is a dimension argument, not an asserted efficient encoder.

**Source pointers.** [Wilde v8][wilde], §§4.4 and 5.2 for the channel/isometry interpretation only; [Weighted kernel](../science/weighted-kernel.md), proof of Theorem 1 and (W3)–(W5), including its pinned algebraic antecedent.

### M16. Weighting the kernel by excitation

**Central question.** What changes when dark vectors are counted according to their excitation instead of all receiving equal weight?

**Understanding target.** The partition function $`Z_G(z)=\sum_k d_kz^k`$ weights each excitation sector. Multiplying the sector inequality by $`z^k`$ and summing introduces one convergent geometric series for each independent lowering profile. For $`0<z<1`$ this gives

```math
Z_G(z)\ge(1+z)^B(1-z)^r.
```

The alternative successive-kernel proof obtains the same factor by rank-nullity at each constraint. Positivity of $`1-z`$ is essential to that iteration.

**Dependencies and story role.** M10 identifies the relevant sub-half excitation bias, and M15 supplies the graded dimension inequality. This milestone turns the local injection into a global weighted count.

**Conceptual connection.** The factor $`(1-z)^r`$ measures the cost of the constraints at the excitation distribution useful under local loss. It is stronger for that purpose than using only the total dark dimension at $`z=1`$.

**Source pointers.** [Wilde v8][wilde], §24.7.2 for the population selected by damping capacity; [Weighted kernel](../science/weighted-kernel.md), Theorem 1, (W1)–(W6), and the successive-kernel proof.

### M17. Dark Gibbs conditioning as an information cost

**Central question.** How does the weighted count produce a useful channel input rather than just a dimension estimate?

**Understanding target.** The Bernoulli product state has the form $`\tau_p^{\otimes B}=z^{\widehat N}/(1+z)^B`$, with $`z=p/(1-p)`$. Because the dark projector commutes with excitation number, conditioning this state on the kernel defines $`\rho_{G,p}=P_Gz^{\widehat N}/Z_G(z)`$. Its relative entropy from the product reference is exactly minus the logarithm of the dark-space weight, hence at most $`-r\log_2(1-z)`$.

**Dependencies and story role.** M07 and M16 provide relative entropy and the weighted lower bound. This milestone translates algebraic abundance into a controlled information deficit.

**Conceptual connection.** The dark Gibbs state is a mathematical input distribution used in the coding proof. The result does not prescribe replacing an unknown payload by this mixed state or implementing an encoder through physical postselection.

**Source pointers.** [Wilde v8][wilde], §11.8; [Weighted kernel](../science/weighted-kernel.md), Corollary 2 and (W7)–(W8).

### M18. Stationarity cancels the excitation mismatch

**Central question.** Why can a dark-supported input approach the local-loss benchmark even if its mean excitation differs from the optimal product input?

**Understanding target.** Expanding the receiver and environment entropies relative to their damped Bernoulli references yields

```math
I_c=Bf_\eta(p)+[\mu-Bp]f_\eta'(p)-D_Y+D_E.
```

Here $`\mu`$ is the actual input's mean excitation, and $`D_Y,D_E`$ are its output relative entropies from the corresponding product references. At $`p=p_\eta`$ the derivative term vanishes. Data processing bounds $`D_Y`$ by the input relative entropy, while $`D_E\ge0`$ can only improve the lower bound.

**Dependencies and story role.** M06–M07, M10, and M17 provide coherent information, relative entropy, the stationary optimizer, and the dark input. This is the central conversion from weighted counting to useful quantum information.

**Conceptual connection.** The cancellation avoids having to force the dark state's mean excitation to equal $`Bp_\eta`$. It also explains why the optimizer of the independent-loss benchmark is the correct comparison point.

**Source pointers.** [Wilde v8][wilde], §§11.5, 11.8, and 24.7.2; [Capacity](../science/capacity.md), Lemma 2 and (C9)–(C11).

### M19. The finite dark-input capacity bound

**Central question.** What operational rate follows from the weighted input's coherent information?

**Understanding target.** Fix $`1/2<\eta<1`$. Degradability survives the isometric dark-input restriction, so the restricted channel's capacity is its maximum single-letter coherent information. Combining M17–M18 with that fact gives

```math
\max\{0,BQ_{\mathrm{AD}}(\eta)-c_\eta r\}
\le Q_{\mathrm{dark}}(G,\eta)
\le BQ_{\mathrm{AD}}(\eta).
```

Here $`c_\eta=-\log_2(1-z_\eta)`$. The upper bound follows because every dark-input code is an admissible code for the unrestricted product amplitude-damping channel. It is not a converse for all encodings in the original collective-plus-local device.

**Dependencies and story role.** M08–M09 and M13–M18 assemble channel structure, the operational limit, and the proof input. This milestone states the first complete global result of the narrative.

**Conceptual connection.** At fixed $`\eta`$, sublinear profile rank $`r=o(B)`$ removes the collective penalty per emitter in the capacity limit. Efficient realization near that rate remains a separate question.

**Source pointers.** [Wilde v8][wilde], §13.5 and chapter 24; [Capacity](../science/capacity.md), §2, Theorem 3, and (C12)–(C13); [Model](../science/model.md), §4.

### M20. A matching worst-profile rank penalty

**Central question.** Is the linear dependence on the number of collective profiles only an artifact of the proof?

**Understanding target.** Disjoint collective pairs each use two physical emitters but retain exactly one logical amplitude-damping channel in their dark kernel. With $`r`$ such pairs and $`B-2r`$ unconstrained sites, the restricted channel has capacity $`(B-r)Q_{\mathrm{AD}}(\eta)`$. Independent single-site constraints give the same deficit for the full allowed rank range. Together with the uniform upper deficit bound, these examples establish worst-profile order $`\Theta_\eta(r)`$.

**Dependencies and story role.** M04–M05 and M19 supply the pair physics and the uniform capacity bound. This milestone tests the theorem against an admissible family that pays a nonzero cost per profile.

**Conceptual connection.** Matching the order is stronger than proving a vanishing penalty per emitter, but it does not determine the optimal coefficient or the exact worst finite profile. Every constrained or redundant emitter remains in the denominator.

**Source pointers.** [Wilde v8][wilde], §24.7.2; [Capacity](../science/capacity.md), Proposition 4, Corollary 5, and (C14)–(C19).

### M21. Fixed noise and the nonuniform noiseless limit

**Central question.** How can the noisy penalty be linear in rank while noiseless dark-space redundancy contains an extra logarithm?

**Understanding target.** At $`\eta=1`$ the capacity is $`\log_2\dim\mathcal K_G`$ and the inherited worst-profile deficit is $`\Theta(r\log(B/r))`$ for $`1\le r=o(B)`$. At each fixed $`1/2<\eta<1`$, the benchmark and its optimal population differ, giving the linear noisy law. As $`\eta\to1`$, $`p_\eta\to1/2`$ and $`c_\eta`$ diverges, so the bound is not uniform in that limit. Ordinary local loss still imposes the finite positive-capacity horizon $`\kappa t<\ln2`$.

**Dependencies and story role.** M10 and M19–M20 provide the biased optimizer and the noisy rank law. This milestone reconciles the global conclusion with the noiseless dimension theorem and finite-cell continuity.

**Conceptual connection.** Attenuating the normalized dark projector already recovers the qualitative local-loss benchmark when $`r=o(B)`$. The weighted argument improves the finite deficit to $`O_\eta(r)`$; it does not first make that qualitative limit possible or imply that noise increases absolute capacity.

**Source pointers.** [Wilde v8][wilde], §24.7.2; [Weighted kernel](../science/weighted-kernel.md), §4; [Capacity](../science/capacity.md), the unweighted comparison in §4 and the limit discussion in §6.

### M22. Which calibration errors change the protected channel?

**Central question.** Why can large coefficient uncertainty be harmless while a small error in a profile direction needs a bound?

**Understanding target.** Unknown linear combinations of modes inside the supplied span annihilate the same dark space, even if their coefficients change during the hold. Components outside that span can activate collective loss. A generator perturbation can be converted to a channel-error radius by Duhamel's formula and channel contractivity; its general tolerance may depend on collective strength and hold time. Inferring a kernel from estimated coefficients additionally requires a stable rank and an appropriate singular-value gap.

**Dependencies and story role.** M12–M14 identify the channel interface and the exact invariant space. This milestone opens the uncertainty part of the narrative by distinguishing exact structural tolerance from quantitative perturbation control.

**Conceptual connection.** The object that must remain close is the encoded channel, not necessarily every microscopic parameter. Direct channel calibration can avoid an ill-conditioned reconstruction of the many-excitation kernel.

**Source pointers.** [Wilde v8][wilde], §§4.4–4.5 and 9.1 for channel composition and distinguishability; [Robustness](../science/robustness.md), §3 and (R8)–(R11).

### M23. A common code for a fixed unknown cell channel

**Central question.** How can one guarantee a decoder without knowing which nearby channel the device realizes?

**Understanding target.** Use the same nominal dark Gibbs input throughout a certified channel set. Conditional-entropy continuity gives a uniform coherent-information penalty, and the compound-channel theorem supplies one encoder and one decoder for all fixed channels in that set. Every positive rate per emitter below the following bound is achievable:

```math
Q_{\mathrm{AD}}(\eta)-\frac{c_\eta r}{B}
-2\epsilon-\frac{g(\epsilon)}B.
```

Here $`g(\epsilon)=(1+\epsilon)h_2(\epsilon/(1+\epsilon))`$. At fixed $`B`$, the admissible radius need not shrink with the number of repeated cells.

**Dependencies and story role.** M06, M09, M12, M19, and M22 supply the fixed-input bound and the channel neighborhood. This milestone converts the physical error certificate into a uniform coding statement.

**Conceptual connection.** Separate optimized capacities do not by themselves produce a common decoder. The result assumes one unknown channel used independently as a tensor power; arbitrary cell-by-cell switching and correlated dynamical reservoirs require other theorems.

**Source pointers.** [Wilde v8][wilde], §11.5 and chapter 24 for the information and coding framework; [Robustness](../science/robustness.md), Theorem 1 and (R1)–(R7), with its primary compound-coding and continuity references.

### M24. Calibration observations and their resource cost

**Central question.** What can finite calibration data certify, and which assumptions must still be supplied?

**Understanding target.** A direct BB84 score calibration estimates the error of the tested endpoint-and-hold procedure, while complete process tomography can certify a channel neighborhood at a much larger cost. The project's sufficient unrestricted procedure scales as $`O(2^{10B}\epsilon_{\mathrm{cal}}^{-2}\log(2^B/\beta))`$ cell exposures. Confidence failure, trusted preparation/readout bounds, reset quality, and later drift remain explicit. Uniform sampling of stationary deployed pairs can certify their mean task error without asserting a bound on every pair individually.

**Dependencies and story role.** M12 and M22–M23 distinguish operational error, channel uncertainty, and a guarantee conditioned on a valid radius. This milestone gives the uncertainty statement a paid acquisition interface.

**Conceptual connection.** Fixed-cell calibration can be amortized while the promise remains valid; it is not free microscopic knowledge. Current payload labels must remain independent of calibration records, and a one-time fixed confidence leaves the corresponding unconditional qualification.

**Source pointers.** [Wilde v8][wilde], §§4.2, 4.4, and 9.1 for observations and channels; [Robustness](../science/robustness.md), §4 and (R12)–(R16); [Operational advantage](../science/operational-advantage.md), §§1 and 5.

### M25. A dark single-excitation cell with a visible loss flag

**Central question.** Which part of the dark space gives a simple physical route to a useful quantum channel?

**Understanding target.** In the one-excitation sector the collective map is the matrix $`G`$ itself, so its kernel has dimension $`B-r`$. Choose a $`d`$-dimensional code inside that kernel. Uniform local loss either preserves the complete codeword or takes it to the orthogonal vacuum, giving exactly

```math
\rho\longmapsto\eta\rho
 +(1-\eta)|v\rangle\langle v|\mathrm{Tr}\rho.
```

The corresponding achievable physical rate is $`(2\eta-1)\log_2d/B`$ when $`\eta>1/2`$. The explicit three-emitter code demonstrates encoding and final flag extraction.

**Dependencies and story role.** M11 and M13–M14 supply erasure-channel meaning and exact dark invariance. This milestone starts the constructive endpoint route after the information-theoretic capacity guarantee.

**Conceptual connection.** A single-excitation code converts ordinary damping into flagged logical loss and is insensitive to a common excitation phase. It uses a smaller code space than the full capacity argument, so efficient erasure storage does not establish efficient coding near $`Q_{\mathrm{AD}}`$.

**Source pointers.** [Wilde v8][wilde], §24.7.1; [Implementation](../science/implementation.md), Proposition 1, §§3–4, and (I1)–(I8).

### M26. Polynomial endpoints with correction only after storage

**Central question.** Can many exact erasure cells store an arbitrary unknown quantum payload with polynomial boundary algorithms?

**Understanding target.** For $`d=2^\ell`$, each erased cell loses a known block of $`\ell`$ outer-code qubits. A random-stabilizer counting bound and an independent-erasure tail bound establish every rate below $`(2\eta-1)\ell/B`$. A sampled Clifford encoder, final flag measurements, syndrome measurements, and Gaussian elimination give polynomial endpoint work. The guarantee is an efficiently sampled code ensemble with a high-probability performance conclusion, not efficient deterministic certification of a globally good fixed code.

**Dependencies and story role.** M09, M11, and M25 supply the repeated-use rate and the exact flagged channel. This milestone closes the constructive quantum-data route with an actual recovery procedure.

**Conceptual connection.** Erasure locations remove the need to search over unknown error supports. Generic coherent residuals or dephasing can create unflagged errors and therefore do not inherit this decoder. Boundary accuracy, routing, and protected preparation/retrieval windows remain charged physical inputs.

**Source pointers.** [Wilde v8][wilde], chapter 24 and §24.7.1 for coding and erasure capacity; [Implementation](../science/implementation.md), Lemma 2, §§5–7, and (I9)–(I12), with its stabilizer and Clifford-synthesis references.

### M27. A fixed pair under direction error and unknown bright phase

**Central question.** How can a nominal dark encoding remain useful when it is not exactly dark for the realized collective mode?

**Understanding target.** The vacuum-plus-dark pair code has a fixed complete encoder and decoder. Its overlap $`b`$ with the actual bright direction obeys the sharp bound $`b\le\delta^2`$ when each complex coupling has relative error at most $`\delta`$. The decoded survival amplitude is $`A=\sqrt\eta(1-b+bz)`$, with $`|z|\le1`$ including the unknown static bright phase. This gives a hold-interval bound independent of collective strength. An unknown phase between vacuum and dark sectors is a different error and must be controlled or budgeted.

**Dependencies and story role.** M01, M04–M05, M12, and M22 supply coherence, loss, dark geometry, and error scope. This milestone begins the finite-task route, which tolerates errors beyond the exact erasure construction.

**Conceptual connection.** Small projection onto a wrongly calibrated bright direction limits the damage caused by that direction during the hold. The geometry requires a static direction; a constant gate count does not establish boundary control under an unbounded always-on reservoir.

**Source pointers.** [Wilde v8][wilde], §§4.7 and 24.7.2 for channel interpretation; [Operational advantage](../science/operational-advantage.md), §§2–3 and 7, Lemma 1, and (O3)–(O13).

### M28. A classical comparator broad enough to be decisive

**Central question.** What does the quantum retrieval protocol outperform when classical storage is given its strongest natural measurement-and-record strategy?

**Understanding target.** The classical device may jointly process every input before the hold, retain an unlimited classical record, and decode using the entire revealed basis string. EPR source replacement and copying that record turn its strategy into identical-answer BB84 monogamy players, so the imported tail theorem applies beyond product measurements. For arbitrary quantum-data storage, the corresponding classical retained-record channel is entanglement breaking and has Bell-overlap at most $`2^{-k}`$ for a $`k`$-qubit payload.

**Dependencies and story role.** M01–M03, M09, and M12 identify the information that crosses the hold. M26–M27 supply the two quantum constructions whose operational value is being compared.

**Conceptual connection.** The separation concerns retained quantum coherence, not a restriction on classical record size or computational power. The BB84 exponent and the general entanglement-breaking reasoning are established ingredients, distinct from the new capacity-rank argument.

**Source pointers.** [Wilde v8][wilde], §§3.6, 4.2–4.5, and chapter 24 for entanglement and communication interfaces; [Operational advantage](../science/operational-advantage.md), §§1 and 5, Theorem 2 and its primary BB84 references; [Implementation](../science/implementation.md), §6.

### M29. One finite end-to-end separation

**Central question.** Do calibration error, additional storage noise, and endpoint error leave a strict measurable task margin?

**Understanding target.** The pair's BB84 bit error is $`(2-|A|^2-\mathrm{Re}A)/4`$. In-storage dephasing and certified endpoint perturbations add bounded probability error through channel distance. At the stated $`\eta=0.9`$, $`\delta=0.1`$, dephasing budget $`0.02`$, and endpoint budget $`0.01`$, the bound is $`p_*=0.08148259\ldots`$. An acceptance fraction $`0.10`$ lies below the classical threshold $`\gamma_*=(1-1/\sqrt2)/2`$ but above $`p_*`$.

**Dependencies and story role.** M12, M24, and M27–M28 supply error budgets, their certificates, the pair channel, and the unrestricted classical comparison. This milestone combines them into an explicit finite claim.

**Conceptual connection.** For 2,200 independent pairs, quantum acceptance is at least $`0.99114618`$ while classical acceptance is at most $`7.69223\times10^{-10}`$, using 4,400 emitters. Independent nonidentical pairs can be controlled through their mean error. These are conditional theoretical bounds, with calibration confidence and every trial retained in the accounting.

**Source pointers.** [Wilde v8][wilde], §§9.1 and 24.7.2 for channel-to-observable interpretation; [Operational advantage](../science/operational-advantage.md), §§4–6 and (O14)–(O25); [Robustness](../science/robustness.md), §4.1.

### M30. The complete scientific claim and its limits

**Central question.** What useful passive-memory advantage is established when the capacity, uncertainty, and implementation statements are read together?

**Understanding target.** At fixed homogeneous local survival $`1/2<\eta<1`$, arbitrary supplied rank-$`r`$ collective dark constraints impose a worst-profile capacity deficit of order $`r`$ relative to the local-loss benchmark. A fixed-cell uncertainty neighborhood supports a common code, while exact single-excitation cells and the robust pair task provide separate constructive operational guarantees. The weighted finite penalty is the specific quantitative refinement; dark states, amplitude-damping capacity, compound coding, and the classical BB84 bound are attributed ingredients.

**Dependencies and story role.** M13–M29 assemble the mechanism, proof, matching examples, noise limits, calibration costs, endpoints, and classical comparison. This final milestone integrates the narrative into one scoped scientific account.

**Conceptual connection.** The results establish useful finite-time storage without intervention during the hold. They do not establish infinite lifetime, protection against arbitrary correlated noise, an unrestricted capacity converse for bright-sector encodings, or efficient near-capacity coding under generic residual errors. The precise gain remains meaningful because the baseline, rate denominator, repeated-cell assumptions, and physical boundary requirements are all explicit.

**Source pointers.** [Wilde v8][wilde], chapter 24 and §§24.7.1–24.7.2 for the capacity framework; [Scientific map](../science/README.md); [Capacity](../science/capacity.md), §§6–7; [Robustness](../science/robustness.md), §5; [Implementation](../science/implementation.md), §7 and resource summary; [Prior work](../science/prior-work.md).

[wilde]: https://arxiv.org/abs/1106.1445v8
