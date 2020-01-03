from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/is_tree_a_bst.py
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    return True

=======
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
  if tree:
    if not (low_range <= tree.data <= high_range):
      return False
    left = is_binary_tree_bst(tree.left, low_range, tree.data)
    right = is_binary_tree_bst(tree.right, tree.data, high_range)
    return left and right
  return True
>>>>>>> c369a0b... some other problems:epi_judge_python/done/is_tree_a_bst.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
