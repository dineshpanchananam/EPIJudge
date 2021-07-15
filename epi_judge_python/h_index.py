from typing import List

from test_framework import generic_test

def h_index(citations: List[int]) -> int:
  i = 0
  citations.sort(reverse=True)
  for x in citations:
    if x <= i:
      break
    i += 1
  return i

if __name__ == '__main__':
  exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
