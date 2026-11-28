import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Data.Nat.Log
namespace MonomialGaps
open Set
/-- For the q-th-power alphabet the paper orders the 2^k tail words
lexicographically. A gap after each word excludes every point of the spectrum
between that word's representative and the next. This injects the words into
the set of actual connected components, even for a nonclosed spectrum. -/
theorem distinct_components (S : Set ℝ) (k : ℕ) (x : Fin (2^k) → ℝ)
    (inside : ∀ i, x i ∈ S) (ordered : StrictMono x)
    (adjacent_gap : ∀ (i : Fin (2^k)) (h : i.val+1 < 2^k),
      ∃ z : ℝ, x i < z ∧ z < x ⟨i.val+1,h⟩ ∧ z ∉ S) :
    Function.Injective (fun i => connectedComponentIn S (x i)) := by
  have separate (i j : Fin (2^k)) (hij : i < j) :
      connectedComponentIn S (x i) ≠ connectedComponentIn S (x j) := by
    intro eq
    have hn : i.val+1 < 2^k := by omega
    obtain ⟨z,hz,hz',out⟩ := adjacent_gap i hn
    have hj : x j ∈ connectedComponentIn S (x i) := eq.symm ▸ mem_connectedComponentIn (inside j)
    have hlast : x ⟨i.val+1,hn⟩ ≤ x j := ordered.monotone (by exact Nat.succ_le_of_lt hij)
    have hp : IsPreconnected (connectedComponentIn S (x i)) := isPreconnected_connectedComponentIn
    have hzmem := hp.ordConnected.out (mem_connectedComponentIn (inside i)) hj
      (show z ∈ Icc (x i) (x j) from ⟨hz.le,hz'.le.trans hlast⟩)
    exact out (connectedComponentIn_subset S _ hzmem)
  intro i j eq
  rcases lt_trichotomy i j with h|h|h
  · exact (separate _ _ h eq).elim
  · exact h
  · exact (separate _ _ h eq.symm).elim
end MonomialGaps
#print axioms MonomialGaps.distinct_components
