from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(t: BinaryTreeNode) -> List[int]:
  res, prev = [], None
  while t:
    if prev is t.parent:
      # went deeper
      if t.left:  # has left, go left
        nxt = t.left
      else:  # no left
        res.append(t.data)  # take node
        nxt = t.right or t.parent  # go right or up
    elif t.left is prev:  # went up from left node
      res.append(t.data)  # take node
      nxt = t.right or t.parent  # go right or up
    else:  # done with left & right
      nxt = t.parent
    prev, t = t, nxt
  return res

  # ans = []
  # st = []
  # while st or t:
  #   if t:
  #     st.append(t)
  #     t = t.left
  #   else:
  #     t = st.pop()
  #     ans.append(t.data)
  #     t = t.right
  # return ans

#     4
#  2    6
# 1 3  5 7

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_with_parent_inorder.py',
                                   'tree_with_parent_inorder.tsv',
                                   inorder_traversal))
