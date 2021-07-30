from typing import List

from test_framework import generic_test

def find_first_missing_positive(A: List[int]) -> int:
  # s = set(A)
  # n = len(A)
  # for i in range(1, len(A)+2):
  #   if i not in s:
  #     return i
  # return n+1
  # n = len(A)
  # for i in range(n):
  #   if A[i] < 0:
  #     A[i] = 0
  # for a in A:
  #   a = abs(a)
  #   if a > 0:
  #     A[a-1] = -abs(A[a-1])
  #     if A[a-1] == 0:
  #       A[a-1] = -a

  # for i in range(len(A)):
  #   if A[i] >= 0:
  #     return i+1
  # return n+1

  n = len(A)
  for i in range(n):
    while 0 < A[i] <= n and A[i] != A[A[i]-1]:
      A[A[i]-1], A[i] = A[i], A[A[i]-1]
  for i in range(n):
    if A[i] != i+1:
      return i+1
  return n+1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('first_missing_positive_entry.py',
                                   'first_missing_positive_entry.tsv',
                                   find_first_missing_positive))
