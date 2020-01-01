from typing import List

from test_framework import generic_test, test_utils


<<<<<<< HEAD:epi_judge_python/permutations.py
def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
=======
def permutations(A):
  n = len(A)
  if not A:
>>>>>>> ee84769... added run and check:epi_judge_python/done/permutations.py
    return []
  parent = [[A[0]]]
  for i in range(1, n):
    children = []
    elem = A[i]
    for perm in parent:
      for k in range(len(perm)+1):
        children.append(perm[:k] + [elem] + perm[k:])
    parent = children
  return parent


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
