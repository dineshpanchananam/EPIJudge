from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    profit, lowest = 0, float("inf")
    for price in prices:
        profit = max(profit, price - lowest)
        lowest = min(lowest, price)
    return profit


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
