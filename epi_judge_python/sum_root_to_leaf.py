from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def sum_root_to_leaf(root: BinaryTreeNode, so_far=0) -> int:
  if not root:
    return 0
  so_far += so_far+root.data
  if not (root.left or root.right):
    return so_far

  return sum_root_to_leaf(root.left, so_far)+sum_root_to_leaf(
    root.right, so_far)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sum_root_to_leaf.py',
                                   'sum_root_to_leaf.tsv', sum_root_to_leaf))
