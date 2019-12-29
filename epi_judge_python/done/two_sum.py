from typing import List

from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/two_sum.py
def has_two_sum(A: List[int], t: int) -> bool:
    # TODO - you fill in here.
    return True

=======
def has_two_sum(A, t):
  i, j = 0, len(A)-1
  while i <= j:
    if A[i] + A[j] == t:
      return True
    elif A[i] + A[j] < t:
      i += 1
    else:
      j -= 1
  return False
>>>>>>> cf3ad5a... solved some:epi_judge_python/done/two_sum.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
