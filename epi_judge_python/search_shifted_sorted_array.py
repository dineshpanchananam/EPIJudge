from typing import List

from test_framework import generic_test


def search_smallest(A: list[int]) -> int:
  # 3,4,5,1,2
  # 5,1,2,3,4

  l, h = 0, len(A)-1
  while l < h:
    if A[l] < A[h]:
      break
    mid = (l+h)//2
    if A[mid] > A[l]:
      l = mid
    else:
      h = mid
  return l


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main(
      "search_shifted_sorted_array.py",
      "search_shifted_sorted_array.tsv",
      search_smallest,
    ))
