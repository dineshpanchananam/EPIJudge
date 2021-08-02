from typing import List

from test_framework import generic_test

def find_nearest_repetition(paragraph: List[str]) -> int:
  words = {}
  dist = 1 << 60
  for pos, word in enumerate(paragraph):
    if word in words:
      dist = min(dist, pos-words[word])
    words[word] = pos
  return -1 if dist == 1 << 60 else dist

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('nearest_repeated_entries.py',
                                   'nearest_repeated_entries.tsv',
                                   find_nearest_repetition))
