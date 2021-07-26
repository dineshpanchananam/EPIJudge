from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
  bgt, pft = float('inf'), 0
  for price in prices:
    bgt = min(bgt, price)
    pft = max(pft, price-bgt)  # sell
  return pft

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('buy_and_sell_stock.py',
                                   'buy_and_sell_stock.tsv',
                                   buy_and_sell_stock_once))
