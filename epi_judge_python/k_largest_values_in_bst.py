from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
  if not tree or k == 0:
    return []
  rc = find_k_largest_in_bst(tree.right, k)
  if len(rc) == k:
    return rc

  return rc+[tree.data]+find_k_largest_in_bst(tree.left, k-len(rc)-1)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('k_largest_values_in_bst.py',
                                   'k_largest_values_in_bst.tsv',
                                   find_k_largest_in_bst,
                                   test_utils.unordered_compare))
