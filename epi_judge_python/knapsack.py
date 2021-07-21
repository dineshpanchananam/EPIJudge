import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
  w = capacity
  n = len(items)
  dp = [[0]*(w+1) for _ in '--']
  for i in range(1, n+1):
    it = items[i-1]
    for j in range(1, w+1):
      dp[1][j] = dp[0][j]
      if it.weight <= j:
        dp[1][j] = max(dp[1][j], it.value+dp[0][j-it.weight])
    dp = dp[::-1]
  return dp[0][-1]

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
  items = [Item(*i) for i in items]
  return executor.run(
    functools.partial(optimum_subject_to_capacity, items, capacity))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                   optimum_subject_to_capacity_wrapper))
