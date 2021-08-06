import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def rotate_array(rotate_amount: int, A: List[int]) -> None:
  n = len(A)
  rotate_amount %= max(1, n)
  if not rotate_amount:
    return
  k = rotate_amount
  copy = A[-k:]
  for i in range(n-k):
    A[n-1-i] = A[n-1-k-i]
  for i in range(k):
    A[i] = copy[i]

@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
  a_copy = A[:]
  executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
  return a_copy

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                   rotate_array_wrapper))
