import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    freq: dict[str, int] = defaultdict(int)
    for ch in data:
        freq[ch] += 1
    return dict(freq)

def build_huffman_tree(frequency: dict[str, int]) -> Optional[HuffmanNode]:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    if not frequency:
        return None

    heap: list[HuffmanNode] = [HuffmanNode(ch, f) for ch, f in frequency.items()]
    heapq.heapify(heap)

    # Special case: only one unique character
    if len(heap) == 1:
        only = heapq.heappop(heap)
        root = HuffmanNode(None, only.freq)
        root.left = only
        return root

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        merged = HuffmanNode(None, lo.freq + hi.freq)
        merged.left = lo
        merged.right = hi
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = code or "0"
        return
    generate_huffman_codes(node.left,  code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)

def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if not data:
        return ("", None)

    frequency = calculate_frequencies(data)
    tree = build_huffman_tree(frequency)
    codes: dict[str, str] = {}
    generate_huffman_codes(tree, "", codes)

    encoded = "".join(codes[ch] for ch in data)
    return (encoded, tree)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not encoded_data or tree is None:
        return ""

    decoded: list[str] = []
    node = tree

    for bit in encoded_data:
        node = node.left if bit == "0" else node.right
        if node and node.char is not None:
            decoded.append(node.char)
            node = tree

    return "".join(decoded)


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    data = "aaaa"
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert data == decoded_data  # single unique character

    # Test Case 3
    encoded_data, tree = huffman_encoding("")
    assert encoded_data == "" and tree is None  # empty string
    assert huffman_decoding(encoded_data, tree) == ""