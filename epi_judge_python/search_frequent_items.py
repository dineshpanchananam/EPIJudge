from typing import Iterator, List
from collections import Counter
import itertools
from test_framework import generic_test, test_utils

# Finds the candidates which may occur > n / k times.
def search_frequent_items(k: int, stream: Iterator[str]) -> List[str]:
  n, c = 0, Counter()
  stream, stream2 = itertools.tee(stream)
  for s in stream:
    c[s] += 1
    n += 1
    if len(c) == k:
      for key in c:
        c[key] -= 1
      c = +c

  # clear contents
  for x in c:
    c[x] = 0

  for s in stream2:
    if s in c:
      c[s] += 1
  return [x for x, v in c.items() if v > n//k]

def search_frequent_items_wrapper(k, stream):
  return search_frequent_items(k, iter(stream))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_frequent_items.py',
                                   'search_frequent_items.tsv',
                                   search_frequent_items_wrapper,
                                   test_utils.unordered_compare))
