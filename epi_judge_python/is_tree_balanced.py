from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def helper(tree):
  if not tree:
    return True, 0
  lb, lh = helper(tree.left)
  rb, rh = helper(tree.right)
  height = 1+max(lh, rh)
  return (lb and rb and abs(lh-rh) <= 1), 1+max(lh, rh)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
  is_bal, _ = helper(tree)
  return is_bal


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_tree_balanced.py',
                                   'is_tree_balanced.tsv',
                                   is_balanced_binary_tree))
