from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
  ans, max_so_far = 0, 0
  for x in A:
    max_so_far = max(x, max_so_far+x)
    ans = max(ans, max_so_far)
  return ans


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_sum_subarray.py',
                                   'max_sum_subarray.tsv',
                                   find_maximum_subarray))
