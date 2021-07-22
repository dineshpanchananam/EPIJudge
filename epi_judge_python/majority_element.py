from typing import Iterator

from test_framework import generic_test

def majority_search(stream: Iterator[str]) -> str:
  mjr, c = None, 1
  # boyer moore
  for s in stream:
    if s == mjr:
      c += 1
    else:
      c -= 1
    if c == 0:
      mjr, c = s, 1
  return mjr

def majority_search_wrapper(stream):
  return majority_search(iter(stream))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('majority_element.py',
                                   'majority_element.tsv',
                                   majority_search_wrapper))
