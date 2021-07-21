from typing import List

from test_framework import generic_test
from two_sum import has_two_sum


def has_three_sum(A: List[int], t: int) -> bool:
  return any(has_two_sum(A, t-a) for a in A)


def has_three_sum_1(A: List[int], t: int) -> bool:
  A.sort()
  n = len(A)
  for i in range(n):
    t0 = t-A[i]
    j, k = i, n-1
    while j <= k:
      s = A[j]+A[k]
      if s == t0:
        return True
      elif s < t0:
        j += 1
      else:
        k -= 1
  return False


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                   has_three_sum))
