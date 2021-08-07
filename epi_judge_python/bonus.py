from typing import List
import heapq
from test_framework import generic_test


def calculate_bonus(productivity: List[int]) -> int:
    n = len(productivity)
    devs = [(p, i) for i, p in enumerate(productivity)]
    heapq.heapify(devs)
    tickets = [1] * n
    while devs:
        d, i = heapq.heappop(devs)
        if i > 0 and d > productivity[i - 1]:
            tickets[i] = tickets[i - 1] + 1
        if i < n - 1 and d > productivity[i + 1]:
            tickets[i] = max(tickets[i], 1 + tickets[i + 1])

    return sum(tickets)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("bonus.py", "bonus.tsv", calculate_bonus))
