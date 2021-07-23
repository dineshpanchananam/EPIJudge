from typing import List

from test_framework import generic_test

import heapq as h

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
  heap = [[a[0], a, 1] for a in sorted_arrays if a]
  h.heapify(heap)
  sortd = []
  while heap:
    x, a, next_idx = h.heappop(heap)
    sortd.append(x)
    if next_idx < len(a):
      h.heappush(heap, [a[next_idx], a, next_idx+1])
  return sortd

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sorted_arrays_merge.py',
                                   'sorted_arrays_merge.tsv',
                                   merge_sorted_arrays))
