from typing import List

from test_framework import generic_test

def find_all_substrings(s: str, words: List[str]) -> List[int]:
  mp = set()
  if not s:
    return []
  n = len(s)
  last = ''
  for i in range(n):
    last += s[i]
    if last 

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'string_decompositions_into_dictionary_words.py',
      'string_decompositions_into_dictionary_words.tsv', find_all_substrings))
