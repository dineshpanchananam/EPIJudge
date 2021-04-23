from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
  s = [tree]
  path = []
  while s:
    if node := s.pop():
      path += node.data,
      s += node.right, node.left
  return path

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                   preorder_traversal))
