from typing import List

from test_framework import generic_test

def can_reach_end(A: List[int]) -> bool:
  mx, last = 0, len(A)-1
  i = 0
  while i <= last and i <= mx < last:
    mx = max(mx, A[i]+i)
    i += 1
  return mx >= last

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('advance_by_offsets.py',
                                   'advance_by_offsets.tsv', can_reach_end))
