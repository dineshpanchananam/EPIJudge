from typing import List

from test_framework import generic_test

def rotate_matrix(a: List[List[int]]) -> None:
  n = len(a)
  for k in range(n//2):
    for i in range(k, n-k-1):
      (
        a[k][i],
        a[i][n-1-k],
        a[n-1-k][n-1-i],
        a[n-1-i][k],
      ) = (
        a[n-1-i][k],
        a[k][i],
        a[i][n-1-k],
        a[n-1-k][n-1-i],
      )

def rotate_matrix_wrapper(square_matrix):
  rotate_matrix(square_matrix)
  return square_matrix

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('matrix_rotation.py', 'matrix_rotation.tsv',
                                   rotate_matrix_wrapper))
