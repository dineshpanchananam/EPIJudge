from typing import List

from test_framework import generic_test, test_utils

<<<<<<< HEAD:epi_judge_python/combinations.py

def combinations(n: int, k: int) -> List[List[int]]:
    # TODO - you fill in here.
    return []

=======
def combinations(n, k):
  if n == 0 or k == 0 or k > n:
    return [[]]
  takeN = combinations(n-1, k-1)
  leaveN = combinations(n-1, k)
  for p in takeN:
    p.append(n)
  return [x for x in takeN + leaveN if x]
>>>>>>> 4b1174a... more problems:epi_judge_python/done/combinations.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
