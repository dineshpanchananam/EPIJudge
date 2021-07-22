from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
  def helper(pi, pj, ii, ij, indent=0):
    if ij < ii:
      return None
    elif ii == ij:
      return BinaryTreeNode(preorder[pi])

    root = preorder[pi]
    count = 0
    for k in range(ii, ij+1):
      if inorder[k] == root:
        break
      count += 1

    return BinaryTreeNode(
      root,
      left=helper(pi+1, pi+count, ii, ii+count-1),
      right=helper(pi+count+1, pj, ii+count+1, ij),
    )

  return helper(0, len(preorder)-1, 0, len(inorder)-1)

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
