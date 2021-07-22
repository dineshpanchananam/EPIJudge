from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
  def helper(po, io, i, j):
    if not j == i:
      return None
    root = preorder[0]
    idx = inorder.index(root)
    return BinaryTreeNode(
      root,
      left=binary_tree_from_preorder_inorder(preorder[1:1+idx], inorder[:idx]),
      right=binary_tree_from_preorder_inorder(preorder[idx+1:],
                                              inorder[idx+1:]),
    )

  return helper(preorder, inorder, 0, len(inorder)-1)

# def binary_tree_from_preorder_inorder(preorder: List[int],
#                                       inorder: List[int]) -> BinaryTreeNode:
#   if not preorder:
#     return None
#   root = preorder[0]
#   idx = inorder.index(root)
#   return BinaryTreeNode(
#     root,
#     left=binary_tree_from_preorder_inorder(preorder[1:1+idx], inorder[:idx]),
#     right=binary_tree_from_preorder_inorder(preorder[idx+1:], inorder[idx+1:]),
#   )

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                   'tree_from_preorder_inorder.tsv',
                                   binary_tree_from_preorder_inorder))
