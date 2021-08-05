from typing import List

from test_framework import generic_test

def bs(a, k, l, h):
  while l <= h:
    mid = (l+h)//2
    if a[mid] == k:
      return mid
    elif a[mid] > k:
      h -= 1
    else:
      l += 1
  return -1

def binary_search_unknown_length(A: List[int], k: int) -> int:
  factor = 1
  offset = 0
  while factor:
    try:
      if A[offset+factor-1] < k:
        offset += factor
        factor *= 2
      else:
        return bs(A, k, offset, offset+factor)
    except IndexError:
      factor //= 2
  return -1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_unknown_length_array.py',
                                   'search_unknown_length_array.tsv',
                                   binary_search_unknown_length))
