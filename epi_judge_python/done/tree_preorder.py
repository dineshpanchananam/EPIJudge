from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/tree_preorder.py
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    return []


=======
def preorder_traversal(tree):
  data = []
  if tree:
    data = [tree.data]
    data += preorder_traversal(tree.left)
    data += preorder_traversal(tree.right)
  return data
  
>>>>>>> ee84769... added run and check:epi_judge_python/done/tree_preorder.py
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
