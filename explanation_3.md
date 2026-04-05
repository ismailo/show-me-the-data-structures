
## Reasoning Behind Decisions:

A heapq min-heap was used as the priority queue because it provides O(log n) push and pop, which is optimal for repeatedly extracting the two lowest-frequency nodes during tree construction. Each node stores char (None for internal nodes) and freq, with __lt__ defined so the heap can compare nodes directly. The generate_huffman_codes function performs a DFS, appending '0' for left and '1' for right until it reaches a leaf. Two critical edge cases required explicit handling: (1) an empty string returns ("", None) immediately with no tree built; (2) a string with only one unique character (e.g., "aaaa") would leave a single node in the heap with no partner to merge — this is handled by wrapping that lone leaf in a synthetic root so that decoding still works correctly (the code becomes repeated '0's).

## Time Efficiency:

Frequency calculation: O(n) — single pass over the input string.
Tree construction: O(k log k) where k is the number of unique characters. Each of the k nodes is pushed and popped from the heap, and each heap operation costs O(log k).
Code generation: O(k) — DFS visits each node in the tree once.
Encoding: O(n) — each character is replaced with its pre-computed code in one pass.
Decoding: O(n) — each bit drives one step down the tree; each leaf visit appends one character.
Overall: O(n + k log k), which simplifies to O(n) since k ≤ n and k is bounded by the alphabet size (at most 256 for ASCII).

## Space Efficiency:

O(k) for the frequency table, heap, code dictionary, and Huffman tree (all proportional to the number of unique characters).
O(n) for the encoded and decoded strings (proportional to input length).
Overall: O(n + k) ≈ O(n).