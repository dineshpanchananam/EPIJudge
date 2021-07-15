from typing import List

from test_framework import generic_test

def h_index(citations: List[int]) -> int:
  # i = 0
  # while True:
  #   c = sum(1 for x in citations if x > i) # O(n)
  #   if c <= i:
  #     break
  #   i += 1
  # return i

  # h = 0
  # for x in sorted(citations, reverse=True):
  #   if x <= h:
  #     break
  #   h += 1
  # return h

  h = 0
  citations.sort(reverse=True)
  a, b = 0, len(citations)-1
  while a <= b:
    mid = (a+b)//2
    if a[mid] > mid:
      h = mid-1
    else:
      l = mid+1

if __name__ == '__main__':
  exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
