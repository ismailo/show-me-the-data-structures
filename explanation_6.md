
## Union Function

## Reasoning Behind Decisions:

Two sets are used — one for each linked list — because sets automatically eliminate duplicates, which is exactly what union requires. Both lists are walked once to populate the sets, then the combined set is used to build the result linked list. Sorted output ensures the result is deterministic.

## Time Efficiency:

O(m + n) — walking list 1 is O(m), walking list 2 is O(n), the set union operation is O(m + n), and rebuilding the linked list is O(m + n).

## Space Efficiency:

O(m + n) — the two sets and the result linked list each hold at most m + n unique elements combined.

## Intersection Function

### Reasoning Behind Decisions:

Each linked list is converted to a set first, so that membership testing costs O(1) instead of O(n). Python's & operator then finds common elements between both sets in one step, replacing what would otherwise be a nested loop of O(m×n) comparisons. The output is sorted before building the result linked list because sets have no guaranteed iteration order in Python — without sorting, the same input could produce a different output ordering on different runs, making testing and verification unreliable.

### Time Efficiency:

O(m + n) — walking list 1 is O(m), walking list 2 is O(n), and the set intersection & is O(min(m, n)) since Python checks the smaller set against the larger.

### Space Efficiency:
O(m + n) — the two intermediate sets take O(m) and O(n), and the result linked list holds at most min(m, n) elements.