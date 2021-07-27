from typing import List

from test_framework import generic_test

def matrix_in_spiral_order(a: List[List[int]]) -> List[int]:
  n = len(a)
  res = []
  for i in range(n//2):
    ab, bc, cd, da = [], [], [], []
    for k in range(i, n-1-i):
      ab.append(a[i][k])
      bc.append(a[k][n-1-i])
      cd.append(a[n-1-i][n-1-k])
      da.append(a[n-1-k][i])
    res += ab+bc+cd+da

  if n & 1:
    res.append(a[n//2][n//2])

  return res

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('spiral_ordering.py', 'spiral_ordering.tsv',
                                   matrix_in_spiral_order))
