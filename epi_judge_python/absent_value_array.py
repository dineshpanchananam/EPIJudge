from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools

def find_missing_element(stream: Iterator[int]) -> int:
  B = 1 << 16
  counter = [0]*B
  stream, copy = itertools.tee(stream)
  for x in stream:
    counter[x >> 16] += 1
  candidate = next(i for i, c in enumerate(counter) if c < B)
  candidate_ips = [0]*B
  for ip in copy:
    if (ip >> 16) == candidate:
      lsb = ip & ((1 << 16)-1)
      candidate_ips[lsb] = 1
  for i, lsb in enumerate(candidate_ips):
    if lsb == 0:
      return (candidate << 16) | i

def find_missing_element_wrapper(stream):
  try:
    res = find_missing_element(iter(stream))
    if res in stream:
      raise TestFailure('{} appears in stream'.format(res))
  except ValueError:
    raise TestFailure('Unexpected no missing element exception')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('absent_value_array.py',
                                   'absent_value_array.tsv',
                                   find_missing_element_wrapper))
