from typing import List

from test_framework import generic_test

def find_kth_in_two_sorted_arrays(a: List[int], b: List[int], k: int) -> int:
  i, j = 0, 0
  m, n = len(a), len(b)
  kth = None
  for _ in range(k):
    if i < m and j < n:
      if a[i] < b[j]:
        kth, i = a[i], i+1
      else:
        kth, j = b[j], j+1
    elif i < m:
      kth, i = a[i], i+1
    else:
      kth, j = b[j], j+1

  return kth

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'kth_largest_element_in_two_sorted_arrays.py',
      'kth_largest_element_in_two_sorted_arrays.tsv',
      find_kth_in_two_sorted_arrays))
