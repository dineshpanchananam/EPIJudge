from typing import List

from test_framework import generic_test

# 4 5 1 2 3
# 5 1 2 3 4

# 1 2 3 4 5
# 3 4 5 1 2

# 2 3 4 5 1

# 4 1 2 3

def search_smallest(a: List[int]) -> int:
  l, h = 0, len(a)-1
  while l < h:
    mid = (l+h)//2
    # print(f"[{l=} {h=}] {mid=} {a[mid]}")
    if a[mid] > a[h]:
      l = mid+1
    else:
      h = mid

  return l

if __name__ == '__main__':
  # print(search_smallest([5, 1, 2, 3, 4]))
  exit(
    generic_test.generic_test_main('search_shifted_sorted_array.py',
                                   'search_shifted_sorted_array.tsv',
                                   search_smallest))
