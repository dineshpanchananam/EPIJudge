import collections
from typing import List

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_longest_increasing_subarray(A: List[int]) -> Subarray:
  A.append(float('-inf'))
  n = len(A)
  streak, mx = 1, 1
  ans = 0
  for i in range(1, n):
    if A[i] > A[i-1]:
      streak += 1
    else:
      if streak > mx:
        mx, ans = streak, i-1
      streak = 1
  return Subarray(ans-mx+1, ans)

def find_longest_increasing_subarray_wrapper(A):
  result = find_longest_increasing_subarray(A)
  return result.end-result.start+1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('longest_increasing_subarray.py',
                                   'longest_increasing_subarray.tsv',
                                   find_longest_increasing_subarray_wrapper))
