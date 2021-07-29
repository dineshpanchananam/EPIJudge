from typing import List

from test_framework import generic_test

def has_dups(su, r, c):
  s = set()
  for i in range(r, r+3):
    for j in range(c, c+3):
      if not su[i][j]:
        continue
      if su[i][j] in s:
        return True
      s.add(su[i][j])
  return False

def conflict(su, x, y):
  v = su[x][y]
  for i in range(9):
    if (i != y and su[x][i] == v) or (i != x and su[i][y] == v):
      return True
  return False

def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
  su = partial_assignment
  for r in range(0, 9, 3):
    for c in range(0, 9, 3):
      if has_dups(su, r, c):
        return False
      for x in range(r, r+3):
        for y in range(c, c+3):
          if not su[x][y]:
            continue
          if conflict(su, x, y):
            return False
  return True

if __name__ == '__main__':
  x = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 0, 0, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0], [6, 0, 3, 0, 0, 0, 0, 0, 2],
       [0, 0, 7, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 9],
       [4, 0, 0, 0, 0, 0, 0, 0, 1], [0, 6, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 0, 0, 0, 0, 0]]
  is_valid_sudoku(x)
  exit(
    generic_test.generic_test_main('is_valid_sudoku.py', 'is_valid_sudoku.tsv',
                                   is_valid_sudoku))
