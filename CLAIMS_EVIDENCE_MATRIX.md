# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Catalog statement and source scope | [Original paper](https://doi.org/10.1016/j.indag.2026.03.008) and [pinned catalog](https://github.com/10m-u/open-problems-catalog/blob/ca8d4d44ba3db527f19f28928c240168f545ecfe/problems/mathematics/differential-equations-dynamical-systems.md#q1537) |
| Theorem | [Analytic manuscript](paper/manuscript.pdf) |
| Prior art and scope | [Literature](audits/public_safe_reports/LITERATURE.md) |
| Illustration and replay | [Worked example](proof/worked-example.md) and [replay output](verification/results/replay.txt) |

**Partial formalization.** For any real spectrum, a realized increasing list of 2^k representatives with a missing spectrum point in each adjacent gap gives an injection of those representatives into its genuine connected components, including for a nonclosed spectrum. The eigenfunction and pressure estimates establishing these gaps for the monomial digits, and the choice of k as a function of q, are in the manuscript. [Lean source](formal/closing/Certificate.lean)
