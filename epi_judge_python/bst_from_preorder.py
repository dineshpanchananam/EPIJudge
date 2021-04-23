from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(seq: List[int]):
  if not seq:
    return
  root = seq[0]
  i, n = 1, len(seq)
  while i < n and seq[i] <= root:
    i += 1
  left = rebuild_bst_from_preorder(seq[1:i])
  right = rebuild_bst_from_preorder(seq[i:])
  return BstNode(root, left, right)


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('bst_from_preorder.py',
                                   'bst_from_preorder.tsv',
                                   rebuild_bst_from_preorder))
