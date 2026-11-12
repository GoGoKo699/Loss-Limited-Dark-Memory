# Scientific map

The central question is whether removing collective radiative loss still leaves a useful quantum memory once local loss and imperfect calibration are charged. The answer has three complementary levels: a uniform capacity law, a finite channel-uncertainty extension, and explicit endpoint constructions.

## The connected argument

1. **[Model and exact reduction](model.md).** Define the passive interval, the common dark kernel, the physical generators, the local-loss benchmark, and the repeated-cell operational limit. Show that homogeneous independent loss preserves the common kernel, so collective loss stays inactive throughout storage.
2. **[Weighted common kernel](weighted-kernel.md).** Refine the commuting-nilpotent injection by excitation number. Convert the sector inequalities into a lower bound on the dark partition function.
3. **[Capacity and rank law](capacity.md).** Select a dark Gibbs input matched to the optimal amplitude-damping population. Use relative-entropy data processing and stationarity to prove the finite capacity penalty, then match its rank dependence with pair and single-site profiles.
4. **[Robustness](robustness.md).** Translate a certified finite-cell channel neighborhood into one common coding guarantee. Distinguish channel uncertainty from changing or correlated cells and relate the neighborhood to physical generator errors.
5. **[Implementation](implementation.md).** Charge encoding, decoding, calibration and precision resources. Develop the single-excitation erasure construction and delimit what efficient endpoints do and do not establish.
6. **[Operational quantum advantage](operational-advantage.md).** Specify delayed-basis retrieval, its unrestricted classical measurement-and-record comparator, the two-emitter encoder and decoder, and a finite calibration/noise budget.
7. **[Prior work](prior-work.md).** Separate the inherited dark-space, amplitude-damping, error-correction and compound-coding ingredients from the excitation-weighted capacity penalty.

## What the results jointly mean

A large ideal dark space alone does not make independent damping disappear. The useful question is how much additional capacity the darkness constraint costs after local loss has already set the baseline. At fixed nonzero loss, the answer is linear in the number of collective profiles. The finite uncertainty result applies to a fixed repeated cell; it does not require the calibration error to vanish as the number of cells grows.

The endpoint constructions address a different resource question. A single-excitation dark block makes a loss detectable as vacuum, so an ordinary erasure decoder can be used after the hold. A smaller vacuum-plus-dark pair has a directly calculated advantage on delayed-basis retrieval, including errors outside the exact symmetry model. Neither construction is asserted to attain the near-benchmark rate of the full common-kernel theorem.

All asymptotic rates count physical emitters and use the ordinary reliability limit over many independently repeated finite cells. All finite numerical checks are documented in [verification](../verification/README.md). No simulation substitutes for the algebraic or coding proof.
