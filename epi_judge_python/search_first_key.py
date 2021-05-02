from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
  idx = -1
  l, h = 0, len(A)-1
  while l <= h:
    mid = (l+h)//2
    if A[mid] < k:
      l = mid+1
      continue
    h = mid-1
    if A[mid] == k:
      idx = mid

  return idx


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_first_key.py',
                                   'search_first_key.tsv', search_first_of_k))
