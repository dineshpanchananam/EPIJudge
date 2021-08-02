from typing import List

from test_framework import generic_test

def matrix_search(A: List[List[int]], x: int) -> bool:
  m, n = len(A), len(A[0])
  i, j = 0, n-1
  while i < m and j >= 0:
    if A[i][j] == x:
      return True
    elif A[i][j] > x:
      j -= 1
    else:
      i += 1
  return False

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                   'search_row_col_sorted_matrix.tsv',
                                   matrix_search))
