from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree, so_far=0) -> int:
  if not tree:
    return 0
  so_far = data*2+tree.data
  if not (tree.left or tree.right):
    return so_far
  return sum_root_to_leaf(tree.left, so_far)+sum_root_to_leaf(
    tree.right, so_far)


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("sum_root_to_leaf.py",
                                   "sum_root_to_leaf.tsv", sum_root_to_leaf))
