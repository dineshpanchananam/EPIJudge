from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/sum_root_to_leaf.py
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.
=======
def sum_root_to_leaf(tree, partial_path_sum=0):
  if not tree:
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/sum_root_to_leaf.py
    return 0
  include_self = (partial_path_sum << 1) + tree.data
  left = sum_root_to_leaf(tree.left, include_self)
  right = sum_root_to_leaf(tree.right, include_self)
  return (left + right) or include_self

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
