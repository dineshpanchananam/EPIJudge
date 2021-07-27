from typing import List

from test_framework import generic_test

def plus_one(A: List[int]) -> List[int]:
  n = len(A)
  c = 1
  for i in range(n-1, -1, -1):
    c += A[i]
    A[i] = c%10
    c //= 10
  # return [c]+A if c else A
  if c:
    A[0] = 1
    A.append(0)
  return A

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('int_as_array_increment.py',
                                   'int_as_array_increment.tsv', plus_one))
