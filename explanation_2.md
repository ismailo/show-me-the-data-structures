
## Reasoning Behind Decisions:

A recursive depth-first search was the natural fit because a directory tree is itself a recursive structure — each directory can contain files and further directories to arbitrary depth. At each level, os.listdir() returns the direct children; os.path.isfile() and os.path.isdir() classify them. Matching files are appended to the result list; directories trigger a recursive call. os.walk() was explicitly prohibited, so this hand-rolled DFS is the correct approach. Edge cases (empty suffix, non-existent path, suffix that matches nothing) are guarded at the top of the function so callers always receive a list and never a crash.

## Time Efficiency:

O(N) where N is the total number of filesystem entries (files + directories) beneath the root path. Every entry is visited exactly once; the endswith() check is O(k) where k is the suffix length, which is constant in practice.

## Space Efficiency:

O(D + M) where D is the maximum depth of the directory tree (stack frames held during recursion) and M is the number of matching files stored in the output list. In the worst case of a completely flat directory D = 1; in a deeply nested tree D can be large, but typical filesystems impose a practical limit well within Python's default recursion depth.