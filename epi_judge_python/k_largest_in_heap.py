from typing import List

from test_framework import generic_test, test_utils

import heapq as h

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
  if k <= 0: return []
  hp = A[:k]
  h.heapify(hp)
  for i in range(k, len(A)):
    popped = h.heappushpop(hp, A[i])
  return hp

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('k_largest_in_heap.py',
                                   'k_largest_in_heap.tsv',
                                   k_largest_in_binary_heap,
                                   comparator=test_utils.unordered_compare))
