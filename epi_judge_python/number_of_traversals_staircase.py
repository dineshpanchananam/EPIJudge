from test_framework import generic_test
from functools import lru_cache


@lru_cache
def number_of_ways_to_top_1(top: int, maximum_step: int) -> int:
  if not top:
    return 1
  ans = 0
  for i in range(1, maximum_step+1):
    if top >= i:
      ans += number_of_ways_to_top(top-i, maximum_step)
  return ans


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
  dp = [1]+[0]*top
  for i in range(top+1):
    for s in range(1, maximum_step+1):
      if i-s >= 0:
        dp[i] += dp[i-s]
  return dp[-1]


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('number_of_traversals_staircase.py',
                                   'number_of_traversals_staircase.tsv',
                                   number_of_ways_to_top))
