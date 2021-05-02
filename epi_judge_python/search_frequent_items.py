from typing import Iterator, List

from test_framework import generic_test, test_utils
from collections import defaultdict


# Finds the candidates which may occur > n / k times.
def search_frequent_items(k: int, stream: Iterator[str]) -> List[str]:
  counts = defaultdict(int)
  total = 0
  for item in stream:
    total += 1
    counts[item] += 1
  result = []
  for number, count in counts.items():
    if count > total//k+1:
      result.append(number)
  return result


def search_frequent_items_wrapper(k, stream):
  return search_frequent_items(k, iter(stream))


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main(
      "search_frequent_items.py",
      "search_frequent_items.tsv",
      search_frequent_items_wrapper,
      test_utils.unordered_compare,
    ))
