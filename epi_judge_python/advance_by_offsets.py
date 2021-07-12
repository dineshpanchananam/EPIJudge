from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
  n, gate = len(A), 0
  for pos in range(n):
    if pos > gate:
      return False
    gate = max(gate, pos+A[pos])
  return gate >= n-1


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("advance_by_offsets.py",
                                   "advance_by_offsets.tsv", can_reach_end))
