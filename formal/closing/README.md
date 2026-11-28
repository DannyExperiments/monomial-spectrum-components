# Separating the component representatives

For any real spectrum, a realized increasing list of 2^k representatives with a missing spectrum point in each adjacent gap gives an injection of those representatives into its genuine connected components, including for a nonclosed spectrum.

The eigenfunction and pressure estimates establishing these gaps for the monomial digits, and the choice of k as a function of q, are in the manuscript.

[Lean proof](Certificate.lean) · [Paper](../../paper/manuscript.pdf)

Run `python3 formal/closing/verify.py` from the repository root with the pinned Lean toolchain and mathlib dependencies available. The workflow sets up those versions, compiles the proof, and checks the names and axioms of the public declarations printed by the file.
