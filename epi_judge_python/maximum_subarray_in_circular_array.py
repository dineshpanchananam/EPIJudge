from typing import List

from test_framework import generic_test


def min_sub_arr_sum(A):
  so_far = ans = float('inf')
  for a in A:
    so_far = min(so_far+a, a)
    ans = min(so_far, ans)
  return ans


def max_subarray_sum_in_circular(A: List[int]) -> int:
  return sum(A)-min_sub_arr_sum(A)


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('maximum_subarray_in_circular_array.py',
                                   'maximum_subarray_in_circular_array.tsv',
                                   max_subarray_sum_in_circular))
