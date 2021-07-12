from typing import List

from test_framework import generic_test


def check_box(grid, x, y):
  s = set()
  for i in range(3):
    for j in range(3):
      if cell := grid[x+i][y+j]:
        if cell not in s:
          s.add(cell)
          continue
        return False
  return True


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      if not check_box(partial_assignment, i, j):
        return False

  row, col = [], []
  for i in range(9):
    for j in range(9):
      if cell := partial_assignment[i][j]:
        row.append(cell)
      if cell := partial_assignment[j][i]:
        col.append(cell)
    for c in (row, col):
      if len(c) != len(set(c)):
        return False
      c.clear()

  return True


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("is_valid_sudoku.py", "is_valid_sudoku.tsv",
                                   is_valid_sudoku))
