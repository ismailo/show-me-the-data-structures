
## Reasoning Behind Decisions:

An iterative depth-first search using an explicit stack was chosen over recursion for two reasons: (1) Python has a default recursion limit (~1000 frames), which could be hit in deeply nested enterprise group hierarchies; (2) an explicit stack gives the same DFS traversal order with no risk of RecursionError. The algorithm starts with the target group on the stack, pops one group at a time, checks whether the user appears in that group's user list, and pushes all sub-groups for further exploration. A None or empty-string user is rejected immediately before the loop, avoiding unnecessary traversal. No visited-group tracking is needed because the Group data structure forms a DAG (directed acyclic graph) by construction — groups cannot contain themselves.

## Time Efficiency:

O(U + G) where U is the total number of users across all groups and G is the total number of groups. In the worst case every group and every user list must be examined before concluding the user is absent.
Early return as soon as the user is found makes the average case faster.

## Space Efficiency:

O(G) for the explicit DFS stack, which at most holds all groups simultaneously in the worst case (a completely flat hierarchy where every sub-group is a direct child of the root).
