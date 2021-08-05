from typing import List

from test_framework import generic_test

def apply_permutation(perm: List[int], a: List[int]) -> None:
  n = len(a)
  # 3 2 0 1
  # a b c d => c d b a
  # 1 2 0 3
  # d b c a
  # b d c a
  # 2 1 0 3
  # c b d a
  # 0 1 2 3
  for i in range(n):
    while perm[i] != i:
      tmp = perm[i]
      a[i], a[tmp] = a[tmp], a[i]
      perm[i], perm[tmp] = perm[tmp], perm[i]

  # aux = [0]*n
  # for i in range(n):
  #   aux[perm[i]] = a[i]
  # a[:] = aux[:]

def apply_permutation_wrapper(perm, A):
  apply_permutation(perm, A)
  return A

if __name__ == '__main__':
  # apply_permutation(
  #   [3, 2, 1, 0],
  #   list('abcd'),
  # )
  exit(
    generic_test.generic_test_main('apply_permutation.py',
                                   'apply_permutation.tsv',
                                   apply_permutation_wrapper))
