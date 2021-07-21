from typing import List

from test_framework import generic_test

def h_index(A: List[int]) -> int:
  A.sort(reverse=True)
  h = 0
  for i in A:
    if i <= h:
      break
    h += 1
  return h

if __name__ == '__main__':
  exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
