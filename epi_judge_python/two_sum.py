from typing import List

from test_framework import generic_test

def has_two_sum(A: List[int], t: int) -> bool:
  # A.sort()
  # i, j = 0, len(A)-1
  # while i <= j:
  #   s = A[i]+A[j]
  #   if s == t:
  #     return True
  #   elif s > t:
  #     j -= 1
  #   else:
  #     i += 1
  # return False

  s = set()
  for x in A:
    s.add(x)
    if t-x in s:
      return True
  return False

if __name__ == '__main__':
  exit(generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                      has_two_sum))
