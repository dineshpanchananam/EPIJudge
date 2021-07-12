from typing import List

from test_framework import generic_test


def search_smallest(a: list[int]) -> int:
  # 2,3,4,5,1
  # 5,1,2,3,4
  l, r = 0, len(a)-1
  while l < r and a[l] > a[r]:
    if (r-l) == 1 and a[l] > a[r]:
      return r
    # print(a, l, r, a[l:r+1])
    # from time import sleep
    # sleep(1)
    mid = (l+r)//2
    if a[mid] < a[l]:
      r = mid
    else:
      l = mid
  return l


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main(
      "search_shifted_sorted_array.py",
      "search_shifted_sorted_array.tsv",
      search_smallest,
    ))
