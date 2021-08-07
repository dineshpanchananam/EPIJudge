from typing import List

from test_framework import generic_test


k = 5
a 1 -2 6 6 -5
p 1 -1 5 11 6
q -1 -1 5 6 6
a=2 b=3
mcs = 7
ml = 3




def find_longest_subarray_less_equal_k(A: List[int], k: int) -> int:
  return 0

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('longest_subarray_with_sum_constraint.py',
                                   'longest_subarray_with_sum_constraint.tsv',
                                   find_longest_subarray_less_equal_k))
