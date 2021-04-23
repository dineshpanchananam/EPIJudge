from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False
    left = remaining_weight - tree.data
    if left == 0 and not (tree.left or tree.right):
        return True
    return has_path_sum(tree.left, left) or has_path_sum(tree.right, left)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum))
