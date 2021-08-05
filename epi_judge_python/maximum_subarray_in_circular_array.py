from typing import List

from test_framework import generic_test

# def min_sub(a):
#   so_far = float('inf')
#   minm = 0
#   for i in a:
#     so_far = min(so_far+i, i)
#     minm = min(so_far, minm)
#   return minm

def max_sub(a):
  so_far = float('-inf')
  maxm = 0
  for i in a:
    so_far = max(so_far+i, i)
    maxm = max(so_far, maxm)
  return maxm

def max_subarray_sum_in_circular(A: List[int]) -> int:
  prefix = max_sub(A)
  suffix = max_sub(-x for x in A)
  return max(prefix, sum(A)+suffix)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('maximum_subarray_in_circular_array.py',
                                   'maximum_subarray_in_circular_array.tsv',
                                   max_subarray_sum_in_circular))
