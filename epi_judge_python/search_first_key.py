from typing import List

from test_framework import generic_test

def search_first_of_k(A: List[int], k: int) -> int:
  l, h = 0, len(A)-1
  idx = -1
  while l <= h:
    m = (l+h)//2
    if A[m] == k:
      idx = m
      h = m-1
    elif A[m] > k:
      h = m-1
    else:
      l = m+1
  return idx

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_first_key.py',
                                   'search_first_key.tsv', search_first_of_k))
