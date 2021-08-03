from typing import Iterator, List

from test_framework import generic_test
import heapq as h

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
  heap = []
  res = []
  for _ in range(k):
    h.heappush(heap, next(sequence))
  for i in sequence:
    res.append(h.heappushpop(heap, i))
  while heap:
    res.append(h.heappop(heap))
  return res

def sort_approximately_sorted_array_wrapper(sequence, k):
  return sort_approximately_sorted_array(iter(sequence), k)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sort_almost_sorted_array.py',
                                   'sort_almost_sorted_array.tsv',
                                   sort_approximately_sorted_array_wrapper))
