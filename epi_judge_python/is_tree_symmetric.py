from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_symmetric(tree: BinaryTreeNode) -> bool:
  def helper(t1, t2):
    if t1 and t2:
      return t1.data == t2.data and helper(t1.left, t2.right) and helper(
        t1.right, t2.left)
    return not (t1 or t2)

  if not tree:
    return True
  return helper(tree, tree)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_tree_symmetric.py',
                                   'is_tree_symmetric.tsv', is_symmetric))
