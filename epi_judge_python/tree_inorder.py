from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal_1(tree):
  s = [(tree, False)]
  result = []
  while s:
    node, left_node_traversed = s.pop()
    if left_node_traversed:
      result.append(node.data)
    elif node:
      s.append((node.right, False))
      s.append((node, True))
      s.append((node.left, False))

  return result

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
  ans = []
  s = []
  while tree or s:
    if tree:
      s.append(tree)
      tree = tree.left
    else:
      tree = s.pop()
      ans.append(tree.data)
      tree = tree.right
  return ans

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("tree_inorder.py", "tree_inorder.tsv",
                                   inorder_traversal))
