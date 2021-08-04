from typing import List

from test_framework import generic_test

def get_max_trapped_water(a: List[int]) -> int:
  l, h = 0, len(a)-1
  area = 0
  while l < h:
    area = max(area, min(a[l], a[h])*(h-l))
    if a[l] > a[h]:
      h -= 1
    else:
      l += 1
  return area

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_trapped_water.py',
                                   'max_trapped_water.tsv',
                                   get_max_trapped_water))
