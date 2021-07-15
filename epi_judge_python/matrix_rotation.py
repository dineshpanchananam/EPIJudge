from typing import List

from test_framework import generic_test

def rotate_matrix(sq: List[List[int]]) -> None:
  n = len(sq)
  for i in range(n//2):
    for k in range(n-i*2-1):
      (
        sq[n-1-i-k][i],
        sq[i][i+k],
        sq[i+k][n-1-i],
        sq[n-1-i][n-1-i-k],
      ) = (
        sq[n-1-i][n-1-i-k],
        sq[n-1-i-k][i],
        sq[i][i+k],
        sq[i+k][n-1-i],
      )

"""
1 2 
3 4
"""
# 3 1
# 4 2

def rotate_matrix_wrapper(square_matrix):
  rotate_matrix(square_matrix)
  return square_matrix

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("matrix_rotation.py", "matrix_rotation.tsv",
                                   rotate_matrix_wrapper))
