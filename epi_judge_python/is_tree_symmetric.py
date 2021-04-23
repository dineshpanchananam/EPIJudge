from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def helper(l, r):
  if not (l or r):
    return True
  if not l or not r:
    return False
  return ((l.data == r.data) and helper(l.right, r.left)
          and helper(l.left, r.right))


def is_symmetric(tree: BinaryTreeNode) -> bool:
  return helper(tree, tree)


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("is_tree_symmetric.py",
                                   "is_tree_symmetric.tsv", is_symmetric))
