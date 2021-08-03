from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(tree):
  ans = []
  st = []
  while tree or st:
    if tree:
      st.append(tree)
      tree = tree.left
    else:
      tree = st.pop()
      ans.append(tree.data)
      tree = tree.right

  return ans

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("tree_inorder.py", "tree_inorder.tsv",
                                   inorder_traversal))
