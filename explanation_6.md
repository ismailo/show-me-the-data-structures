
## Union Function

## Reasoning Behind Decisions:

Two sets are used — one for each linked list — because sets automatically eliminate duplicates, which is exactly what union requires. Both lists are walked once to populate the sets, then the combined set is used to build the result linked list. Sorted output ensures the result is deterministic.

## Time Efficiency:

O(m + n) — walking list 1 is O(m), walking list 2 is O(n), the set union operation is O(m + n), and rebuilding the linked list is O(m + n).

## Space Efficiency:

O(m + n) — the two sets and the result linked list each hold at most m + n unique elements combined.

## Intersection Function

### Reasoning Behind Decisions:

Each linked list is converted to a set first. Python's & operator then finds common elements between both sets in one step. This avoids a nested loop, which would require checking every element of list 1 against every element of list 2. Sorted output keeps the result consistent.

### Time Efficiency:

O(m + n) — walking list 1 is O(m), walking list 2 is O(n), and the set intersection & is O(min(m, n)) since Python checks the smaller set against the larger.

### Space Efficiency:
O(m + n) — the two intermediate sets take O(m) and O(n), and the result linked list holds at most min(m, n) elements.