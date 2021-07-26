from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

def rebuild_bst_from_preorder(xs: List[int]) -> Optional[BstNode]:
  if not xs:
    return None
  root = xs[0]
  i, n = 1, len(xs)
  while i < n and xs[i] < root:
    i += 1
  return BstNode(
    root,
    rebuild_bst_from_preorder(xs[1:i]),
    rebuild_bst_from_preorder(xs[i:]),
  )

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('bst_from_preorder.py',
                                   'bst_from_preorder.tsv',
                                   rebuild_bst_from_preorder))
