from test_framework import generic_test

from functools import lru_cache

@lru_cache
def number_of_ways_to_top(top: int, maximum_step: int) -> int:
  if not top:
    return 1
  ways = 0
  for s in range(1, maximum_step+1):
    if top-s >= 0:
      ways += number_of_ways_to_top(top-s, maximum_step)
  return ways

# def number_of_ways_to_top(top: int, maximum_step: int) -> int:
#   dp = [0]*(top+1)
#   dp[0] = 1
#   for i in range(top+1):
#     for j in range(1, maximum_step+1):
#       if i+j <= top:
#         dp[i+j] += dp[i]
#   return dp[-1]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('number_of_traversals_staircase.py',
                                   'number_of_traversals_staircase.tsv',
                                   number_of_ways_to_top))
