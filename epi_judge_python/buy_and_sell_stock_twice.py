from typing import List

from test_framework import generic_test

def buy_and_sell_stock_twice(prices: List[float]) -> float:
  bgt, prof = float('inf'), 0
  profits = []
  n = len(prices)
  for i in range(n):
    bgt = min(bgt, prices[i])
    prof = max(prof, prices[i]-bgt)
    profits.append(prof)
  max_prof = max(profits)
  sell = float('-inf')
  for i in range(n-1, 1, -1):
    sell = max(sell, prices[i])
    max_prof = max(max_prof, sell-prices[i]+profits[i-1])
  return max_prof

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                   'buy_and_sell_stock_twice.tsv',
                                   buy_and_sell_stock_twice))
