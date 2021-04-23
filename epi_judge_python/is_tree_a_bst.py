from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_bst(t, l, h):
    if not t:
        return True
    return l <= t.data <= h and is_bst(t.left, l, t.data) and is_bst(t.right, t.data, h)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    l, h = float("-inf"), float("inf")
    return is_bst(tree, l, h)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_a_bst.py", "is_tree_a_bst.tsv", is_binary_tree_bst
        )
    )
