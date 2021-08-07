from typing import List

from test_framework import generic_test

def longest_contained_range(A: List[int]) -> int:
  s = set(A)
  res = 0
  for i in A:
    if i-1 in s:
      continue
    seq = 0
    while i in s:
      seq += 1
      res = max(res, seq)
      # s.remove(i)
      i += 1
  return res

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('longest_contained_interval.py',
                                   'longest_contained_interval.tsv',
                                   longest_contained_range))
