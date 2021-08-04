import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
  added = []
  k, n = 0, len(disjoint_intervals)
  while k < n and disjoint_intervals[k].right < new_interval.left:
    added.append(disjoint_intervals[k])
    k += 1

  while k < n and (disjoint_intervals[k].left <= new_interval.right):
    new_interval = Interval(
      min(new_interval.left, disjoint_intervals[k].left),
      max(new_interval.right, disjoint_intervals[k].right),
    )
    k += 1

  return added+[new_interval]+disjoint_intervals[k:]

@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
  disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
  return executor.run(
    functools.partial(add_interval, disjoint_intervals,
                      Interval(*new_interval)))

def res_printer(prop, value):
  def fmt(x):
    return [[e[0], e[1]] for e in x] if x else None

  if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
    return fmt(value)
  else:
    return value

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('interval_add.py',
                                   'interval_add.tsv',
                                   add_interval_wrapper,
                                   res_printer=res_printer))
