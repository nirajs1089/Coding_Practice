from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Compute the diameter (longest path in edges) of a binary tree using
    an explicit stack (iterative post-order traversal) instead of recursion.

    Args:
        root: The root node of the binary tree.

    Returns:
        The diameter of the tree (number of edges in longest path).
    """
    if not root:
        return 0

    # Stack for building post-order: first stack for traversal, second for post-order
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        # Push children onto stack1
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Map to store height of subtree rooted at each node
    height = {}
    max_diameter = 0

    # Process nodes in post-order (children before parent)
    while stack2:
        node = stack2.pop()
        left_h = height.get(node.left, 0)
        right_h = height.get(node.right, 0)

        # Diameter passing through this node is left_h + right_h
        max_diameter = max(max_diameter, left_h + right_h)

        # Height of this node: one plus max of children heights
        height[node] = 1 + max(left_h, right_h)

    return max_diameter

# ───────── Example Usage ─────────
if __name__ == "__main__":
    # Build a sample tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    # The longest path is 4 -> 2 -> 1 -> 3, length = 3 edges
    print(diameter_of_binary_tree(root))  # Expected output: 3
