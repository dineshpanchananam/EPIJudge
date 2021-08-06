import copy
from typing import List

from test_framework import generic_test

def rook_attack(A: List[List[int]]) -> None:
  m, n = len(A), len(A[0])
  cr, cc = 0, 0
  for i in range(n):
    if A[0][i] == 0:
      cr = 1
      break

  for i in range(m):
    if A[i][0] == 0:
      cc = 1
      break

  for i in range(1, m):
    for j in range(1, n):
      if A[i][j] == 0:
        A[i][0] = 0
        A[0][j] = 0

  for i in range(1, n):
    if A[0][i] == 0:
      for j in range(1, m):
        A[j][i] = 0

  for i in range(1, m):
    if A[i][0] == 0:
      for j in range(1, n):
        A[i][j] = 0

  if cc:
    for i in range(m):
      A[i][0] = 0

  if cr:
    for i in range(n):
      A[0][i] = 0

  # rows, cols = set(), set()
  # for i in range(m):
  #   for j in range(n):
  #     if not A[i][j]:
  #       rows.add(i)
  #       cols.add(j)

  # for r in rows:
  #   for c in range(n):
  #     A[r][c] = 0

  # for c in cols:
  #   for r in range(m):
  #     A[r][c] = 0

def rook_attack_wrapper(A):
  a_copy = copy.deepcopy(A)
  rook_attack(a_copy)
  return a_copy

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('rook_attack.py', 'rook_attack.tsv',
                                   rook_attack_wrapper))
