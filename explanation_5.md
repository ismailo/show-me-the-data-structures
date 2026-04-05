
## Reasoning Behind Decisions:

Both functions first convert each linked list into a Python set using a helper method to_set(). Sets provide O(1) average membership testing and built-in | (union) and & (intersection) operators. This avoids the naive O(m·n) nested-loop approach that would be required if membership were tested by walking the list each time. After computing the set result, a helper _build_list() rebuilds a sorted linked list so the output is deterministic regardless of set iteration order. Edge cases covered: one or both lists empty (sets handle this gracefully — union returns the non-empty set, intersection returns an empty set), and duplicate values within a single list (sets deduplicate automatically, matching the mathematical definition of union and intersection).

## Time Efficiency:

to_set(): O(m) or O(n) — single pass over each list.
Set union (|): O(m + n) — Python iterates both sets to build the result.
Set intersection (&): O(min(m, n)) — Python iterates the smaller set and checks membership in the larger.
_build_list(): O(r log r) where r is the result size (for sorting) + O(r) for appending — dominated by O(r log r).
Overall union: O(m + n) — the sort is over at most m + n unique elements.
Overall intersection: O(m + n) — building both sets dominates.


## Space Efficiency:

to_set(): O(m) + O(n) for the two intermediate sets.
Result set: O(m + n) for union; O(min(m, n)) for intersection.
Result linked list: O(r) where r is the number of elements in the result.
Overall: O(m + n) — proportional to the combined input size.