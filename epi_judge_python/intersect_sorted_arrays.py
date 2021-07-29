from typing import List

from test_framework import generic_test

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
  # TODO - you fill in here.
  m, n = len(A), len(B)
  i, j = 0, 0
  c = []
  while i < m and j < n:
    if A[i] == B[j]:
      if not c or c[-1] != A[i]:
        c.append(A[i])
      i, j = i+1, j+1
    elif A[i] < B[j]:
      i += 1
    else:
      j += 1
  return c

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('intersect_sorted_arrays.py',
                                   'intersect_sorted_arrays.tsv',
                                   intersect_two_sorted_arrays))
