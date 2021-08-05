from typing import List

from test_framework import generic_test
import bintrees

def find_closest_elements_in_sorted_arrays(
    sorted_arrays: List[List[int]]) -> int:
  n = len(sorted_arrays)
  min_dist = float('inf')
  rbt = bintrees.RBTree()
  for idx, arr in enumerate(sorted_arrays):
    itr = iter(arr)
    minm = next(itr, None)
    if minm is not None:
      rbt.insert((minm, idx), itr)

  while True:
    min_val, min_idx = rbt.min_key()
    maxm = rbt.max_key()[0]
    min_dist = min(min_dist, maxm-min_val)
    _, v = rbt.pop_min()
    nxt = next(v, None)
    if nxt is None:
      return min_dist
    rbt.insert((nxt, min_idx), v)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                   'minimum_distance_3_sorted_arrays.tsv',
                                   find_closest_elements_in_sorted_arrays))
