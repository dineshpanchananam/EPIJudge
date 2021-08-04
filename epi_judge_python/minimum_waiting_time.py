from typing import List
from functools import reduce
from test_framework import generic_test

def minimum_total_waiting_time(s: List[int]) -> int:
  n = len(s)
  return sum(i*(n-idx) for idx, i in enumerate(sorted(s), 1))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('minimum_waiting_time.py',
                                   'minimum_waiting_time.tsv',
                                   minimum_total_waiting_time))
