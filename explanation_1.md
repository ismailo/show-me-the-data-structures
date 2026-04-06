
## Reasoning Behind Decisions:

An OrderedDict was chosen because it natively combines a hash map with a doubly-linked list under the hood. The hash map gives O(1) key lookup, and the doubly-linked list lets us reorder entries in O(1) without shifting anything. Every get() call moves the accessed key to the "most recently used" end via move_to_end(). Every set() call inserts or updates a key, then evicts the front entry (popitem(last=False)) if the cache exceeds capacity. This matches the LRU contract exactly. A plain dict would not work because Python dicts (while ordered since 3.7) do not expose O(1) reordering. Implementing a custom doubly-linked list + dict would achieve the same result but at the cost of more code with no performance benefit.

## Time Efficiency:

get(): O(1) - hash map lookup + move_to_end() (pointer manipulation, not a scan).
set(): O(1) — hash map insert/update + move_to_end() + optional popitem() (all pointer operations).
Both operations meet the O(1) requirement stated in the problem.

## Space Efficiency:

O(capacity) — the OrderedDict never holds more entries than the declared capacity, so memory is bounded by the cache size regardless of how many set() calls are made.