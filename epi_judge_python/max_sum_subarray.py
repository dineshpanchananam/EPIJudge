from typing import List

from test_framework import generic_test

def find_maximum_subarray(A: List[int]) -> int:
  so_far, ans = 0, 0
  for x in A:
    so_far = max(so_far+x, x)
    ans = max(so_far, ans)
  return ans

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_sum_subarray.py',
                                   'max_sum_subarray.tsv',
                                   find_maximum_subarray))
