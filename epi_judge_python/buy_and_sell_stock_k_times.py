from typing import List

from test_framework import generic_test

def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
  if k == 0:
    return 0.0
  elif 2*k >= len(prices):
    return sum(max(0, b-a) for a, b in zip(prices[:-1], prices[1:]))

  n = len(prices)
  dp = [[0]*n, [0]*n]
  for t in range(1, k+1):
    row = t%2
    so_far = float('-inf')
    for i in range(1, n):
      so_far = max(so_far, dp[row-1][i-1]-prices[i-1])
      dp[row][i] = max(dp[row][i-1], so_far+prices[i])

  return dp[t%2][-1]

if __name__ == '__main__':
  # buy_and_sell_stock_k_times([5, 11, 3, 50, 60, 90], 2)
  # buy_and_sell_stock_k_times(
  #   [0.8, 0.3, 0.8, 0.9, 0.2, 0.9, 0.4, 0.5, 1.0, 0.2], 5)
  exit(
    generic_test.generic_test_main('buy_and_sell_stock_k_times.py',
                                   'buy_and_sell_stock_k_times.tsv',
                                   buy_and_sell_stock_k_times))

# 0  1  2  3  4  5
# -----------------
# 0  0  0  0  0  0
# 0  6  6  47 57 87
# 0  6
