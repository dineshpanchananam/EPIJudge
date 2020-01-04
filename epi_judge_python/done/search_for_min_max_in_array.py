import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


<<<<<<< HEAD:epi_judge_python/search_for_min_max_in_array.py
def find_min_max(A: List[int]) -> MinMax:
    # TODO - you fill in here.
    return MinMax(0, 0)
=======
def find_min_max(A):
  mn, mx = float('inf'), float('-inf')
  for i in A:
    if i > mx:
      mx = i
    if i < mn:
      mn = i
  return MinMax(mn, mx)
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/search_for_min_max_in_array.py


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
