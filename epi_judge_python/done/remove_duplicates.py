import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

<<<<<<< HEAD:epi_judge_python/remove_duplicates.py
    def __lt__(self, other) -> bool:
=======
    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
>>>>>>> 6e7e48e... some wip:epi_judge_python/done/remove_duplicates.py
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)    


<<<<<<< HEAD:epi_judge_python/remove_duplicates.py
def eliminate_duplicate(A: List[Name]) -> None:
    # TODO - you fill in here.
    return

=======
def eliminate_duplicate(A):
  # from operator import le
  assert all(isinstance(x, Name) for x in A)
  n = len(A)
  A.sort()
  i, j = 0, 0
  while j < n:
    if A[i] < A[j]:
      assert i < j
      A[i] = A[j]
      i += 1
    j += 1
  for _ in range(n-i+1):
    A.pop()
  n = len(A)
  assert all(isinstance(x, Name) for x in A)
  for i in range(n):
    A[i] = A[i].first_name
  print("$$", len(A))
>>>>>>> 6e7e48e... some wip:epi_judge_python/done/remove_duplicates.py

@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
