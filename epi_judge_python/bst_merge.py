from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from bst_to_sorted_list import bst_to_doubly_linked_list

def count(l):
  n = 0
  while l:
    n += 1
    l = l.right
  return n

def ll_to_bst(ll, n):
  if n == 0:
    return

  mid = n//2
  left = ll
  for i in range(mid):
    ll = ll.right
  ll.left = ll_to_bst(left, mid)
  ll.right = ll_to_bst(ll.right, n-1-mid)
  return ll

def merge_two_bsts(A: BstNode, B: BstNode) -> Optional[BstNode]:
  A = bst_to_doubly_linked_list(A)
  B = bst_to_doubly_linked_list(B)
  C = c = BstNode()
  while A and B:
    if A.data < B.data:
      c.right = A
      A = A.right
    else:
      c.right = B
      B = B.right
    c = c.right
  c.right = A or B
  n = 0
  c, prev = C.right, None

  return ll_to_bst(C.right, count(C.right))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('bst_merge.py', 'bst_merge.tsv',
                                   merge_two_bsts))
