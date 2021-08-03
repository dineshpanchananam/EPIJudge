from typing import List

from test_framework import generic_test

def maximum_revenue(coins: List[int]) -> int:
  scores = {0: 0, 1: 0}

  def helper(i, j, turn):
    if i > j:
      return 0
    key = f"{i}-{j}-{turn}"
    if key not in cache:
      cache[key] = max(
        coins[i]+helper(i+1, j, turn ^ 1),
        coins[j]+helper(i, j-1, turn ^ 1),
      )
    return cache[key]

  cache = {}
  m, n = 0, len(coins)-1
  print(sum(coins))
  res = helper(m, n, 0)
  print(cache)
  return res

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('picking_up_coins.py',
                                   'picking_up_coins.tsv', maximum_revenue))
