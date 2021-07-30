from typing import List

from test_framework import generic_test
from functools import lru_cache

def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
  @lru_cache
  def search(a, b, c):
    if c == p:
      return True
    if a >= m or a < 0 or b >= n or b < 0:
      return False
    key = f"{a}-{b}-{c}"
    visited.add(key)
    found = False
    if grid[a][b] == pattern[c]:
      for x, y in ((a-1, b), (a+1, b), (a, b-1), (a, b+1)):
        if found: break
        found = search(x, y, c+1)

    visited.remove(key)
    return found

  fnd = False
  m, n = len(grid), len(grid[0])
  p = len(pattern)
  visited = set()
  for i in range(m):
    for j in range(n):
      if fnd: break
      fnd = search(i, j, 0)
  return fnd

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_string_in_matrix.py',
                                   'is_string_in_matrix.tsv',
                                   is_pattern_contained_in_grid))
