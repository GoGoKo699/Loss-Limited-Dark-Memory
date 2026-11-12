# Verification

The written proofs establish the universal results. The scripts independently check finite channel identities, entropy bookkeeping and the numerical working points.

## Reproduce

The inspected environment used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The command recomputes the diagnostics, enforces their mathematical inequalities, and compares the resulting record with [results.json](results.json). Numerical comparison allows small floating-point differences. It does not modify the reference output. Use `--write` only to intentionally regenerate that output after reviewing a scientific change.

## What is checked

| Check | Method | Finite scope |
|---|---|---|
| Weighted partition and coherent-information inequalities | Numerical common-kernel construction for complex profiles; direct output and complementary-output entropies | 21 instances, 2–6 emitters, 1–3 profiles, three local-loss values |
| Darkness throughout local loss | Apply the collective dissipator to independently damped dark states | Same 21 instances |
| Coherent-information identity away from the optimizer | Direct entropies and relative entropies for general mixed states with excitation coherences | Six three-emitter inputs |
| Pair channel with bright phase | Exponentiate the full Lindblad superoperator and compare with the scalar amplitude formula | 24 combinations of misalignment, collective rate and Lamb phase |
| Additional in-storage dephasing | Full simultaneous generator compared with the unperturbed formula and the Duhamel error budget | Four collective rates |
| Single-excitation erasure channel | Exponentiate simultaneous collective/local generators, including a collective Lamb term, on every encoded matrix unit | Four cells, 3 or 4 emitters, two local-loss values |
| Complex calibration disks | Random complex perturbations and the analytic extremizer | 30,000 samples and three exact extremal parameter choices |
| Operational and capacity examples | Evaluate the stated formulas | The two-emitter error margin and the 32-emitter compound-rate lower bound |

In the inspected run, the largest dark-invariance residual was below $`8.4\times10^{-15}`$, the largest pair-formula discrepancy below $`1.7\times10^{-14}`$, and the largest erasure-channel discrepancy below $`8.5\times10^{-16}`$. The committed output records the actual values. Such residuals are diagnostic evidence for the implementations, not error bars on an experimental device or a proof for arbitrary system size.

## Boundaries

The script does not implement an asymptotically optimal common-kernel encoder, reconstruct an actual bath, certify a device's calibration, simulate arbitrarily many cells, or validate the imported coding theorems. Those assumptions and proof dependencies are stated in [the model](../science/model.md), [capacity](../science/capacity.md), [robustness](../science/robustness.md) and [implementation](../science/implementation.md) pages.

`weighted_capacity.py` and `pair_lindblad.py` contain the small-matrix primitives used by the suite. `run_all.py` is the authoritative reproduction command.

## Hosted mathematical presentation

The [read-only workflow](../.github/workflows/hosted-math.yml) checks the exact proposed commit on GitHub at widths of 1,440 and 760 pixels. It first probes the README's inline, display and table notation, then inventories all tracked Markdown and compares every mathematical expression with the actual hosted MathML. The comparison retains operands, relations, subscripts, fractions and meaningful token structure. HTML, screenshots, source inventories and reports are saved together for subsequent visual inspection. A separate viewport collector records unmodified native page details below GitHub's floating toolbar, including the principal capacity formula and the calibration confidence bound. These supplementary screenshots support visual review; they do not replace the full structural comparison.

The collector and checker in [hosted_math/](hosted_math/) use Node.js 22, Playwright 1.56.1, MathJax 3.2.1, Python 3.10 or later, and Git. Dependencies are installed outside the source tree. To repeat a complete capture from a compatible environment, set `NODE_PATH` to those installed Node modules and run:

```bash
node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Loss-Limited-Dark-Memory \
  --revision "$(git rev-parse HEAD)" \
  --output /tmp/loss-limited-dark-memory-hosted
```

Use a new empty output directory and an existing public commit. The workflow checks out the exact same-repository PR head without persisting credentials and grants only `contents: read`. Its captured artifacts expire after fourteen days. A successful automated comparison still requires visual inspection for layout and legibility; it does not validate the physical assumptions or analytical proofs, or guarantee future renderer behavior.
