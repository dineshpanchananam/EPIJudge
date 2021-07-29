from typing import List

from test_framework import generic_test
from random import randint

def part(A):
  i, j = 0, len(A)-1
  p_i = randint(i, j)
  A[0], A[p_i] = A[p_i], A[0]
  pvt = A[0]
  while i <= j:
    if A[i] >= pvt:
      i += 1
    elif A[j] < pvt:
      j -= 1
    else:
      A[j], A[i] = A[i], A[j]
      i, j = i+1, j-1
  A[0], A[j] = A[j], A[0]
  return j

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
  p = part(A)
  if p+1 == k:
    return min(A[:p+1])
  elif k > p+1:
    return find_kth_largest(k-p-1, A[p+1:])
  else:  # k < right+1
    return find_kth_largest(k, A[:p])

# 1 0 0 0 3 4 5

if __name__ == '__main__':
  # a = [3, 4, 1, 2, 5, 6]
  # print(part(a))
  # print(a)
  # a = [3, 1, -1, 2]
  # part(a)
  # print(a)
  # for i in range(1, 5):
  #   print(i, find_kth_largest(i, a))
  #   print(a)
  exit(
    generic_test.generic_test_main('kth_largest_in_array.py',
                                   'kth_largest_in_array.tsv',
                                   find_kth_largest))
