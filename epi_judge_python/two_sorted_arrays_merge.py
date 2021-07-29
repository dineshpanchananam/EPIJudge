from typing import List

from test_framework import generic_test

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
  k = m+n-1
  i, j = m-1, n-1
  while i >= 0 and j >= 0:
    if A[i] >= B[j]:
      A[k] = A[i]
      k, i = k-1, i-1
    else:
      A[k] = B[j]
      k, j = k-1, j-1

  for l, a in ((i, A), (j, B)):
    while l >= 0:
      A[k] = a[l]
      k, l = k-1, l-1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
  merge_two_sorted_arrays(A, m, B, n)
  return A

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                   'two_sorted_arrays_merge.tsv',
                                   merge_two_sorted_arrays_wrapper))
