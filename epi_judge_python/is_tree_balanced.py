from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_balanced(tree: BinaryTreeNode) -> bool:
  if not tree:
    return 0, True
  lh, lb = is_balanced(tree.left)
  rh, rb = is_balanced(tree.right)
  return 1+max(lh, rh), lb and rb and abs(lh-rh) < 2

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
  return is_balanced(tree)[1]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_tree_balanced.py',
                                   'is_tree_balanced.tsv',
                                   is_balanced_binary_tree))
