from typing import List

from test_framework import generic_test

def calculate_trapping_water(a: List[int]) -> int:
  max_h = a.index(max(a))

  def helper(hgts):
    ps, h = 0, float('-inf')
    for x in hgts:
      h = max(x, h)
      ps += h-x
    return ps

  return helper(a[:max_h])+helper(reversed(a[max_h+1:]))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_water_trappable.py',
                                   'max_water_trappable.tsv',
                                   calculate_trapping_water))
