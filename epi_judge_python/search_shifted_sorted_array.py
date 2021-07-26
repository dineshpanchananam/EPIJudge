from typing import List

from test_framework import generic_test

# 4 5 1 2 3

# 1 2 3 4 5
# 3 4 5 1 2

# 5 1 2 3 4
# 2 3 4 5 1

# 4 1 2 3

def search_smallest(A: List[int]) -> int:
  l, h = 0, len(A)-1
  while l < h:
    m = (l+h)//2
    if A[l] < A[m]:
      if A[l] < A[h]:
        l = m+1
      else:  # A[l] > A[r]
        h = m-1
    else:  # A[l] > A[m]
      # if A[l] > A[h]:
      h = m
    # else:
    #   l = m
  print(l, m, h)
  return A[h]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_shifted_sorted_array.py',
                                   'search_shifted_sorted_array.tsv',
                                   search_smallest))
