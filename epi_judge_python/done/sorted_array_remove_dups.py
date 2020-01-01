import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
<<<<<<< HEAD:epi_judge_python/sorted_array_remove_dups.py
def delete_duplicates(A: List[int]) -> int:
    # TODO - you fill in here.
    return 0
=======
def delete_duplicates(A):
  i, j = 0, 0
  n = len(A)
  while j < n:
    if A[i] != A[j]:
      i += 1
      A[i] = A[j]
    j += 1
  return min(i + 1, n)
>>>>>>> ee84769... added run and check:epi_judge_python/done/sorted_array_remove_dups.py


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
