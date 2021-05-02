from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def helper(t, k):
  if (not t) or k == 0:
    return []
  left = helper(t.right, k)
  if len(left) < k:
    left.append(t.data)
  if len(left) < k:
    left.extend(helper(t.left, k-len(left)))
  return left


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
  return helper(tree, k)[::-1]


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('k_largest_values_in_bst.py',
                                   'k_largest_values_in_bst.tsv',
                                   find_k_largest_in_bst,
                                   test_utils.unordered_compare))
