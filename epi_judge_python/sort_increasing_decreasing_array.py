from typing import List

from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
  incr = True
  sub_arrays = []
  start = 0
  for i in range(1, len(A)+1):
    if i == len(A) or (A[i] > A[i-1] and not incr) or (A[i] <= A[i-1]
                                                       and incr):
      if incr:
        sub_arrays.append(A[start:i])
      else:
        sub_arrays.append(A[i-1:start-1:-1])
      incr = not incr
      start = i
  return merge_sorted_arrays(sub_arrays)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                   'sort_increasing_decreasing_array.tsv',
                                   sort_k_increasing_decreasing_array))
