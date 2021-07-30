from typing import List

from test_framework import generic_test

from collections import Counter

def find_all_substrings(s: str, words: List[str]) -> List[int]:
  m = len(words)
  k = len(words[0])
  n = len(s)
  if 0 in [m, n] or len(s) < m*k:
    return []

  mapping = {}
  idx = 0
  for w in words:
    if w not in mapping:
      mapping[w] = idx
      idx += 1
  counts = [0]*len(mapping)
  for w in words:
    counts[mapping[w]] += 1

  ans = []
  for i in range(n-m*k+1):
    c = list(counts)
    for l in range(i, i+m*k, k):
      sub = s[l:l+k]
      if sub not in mapping or not c[mapping[sub]]:
        break
      c[mapping[sub]] -= 1
    if not sum(c):
      ans.append(i)

  return ans

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'string_decompositions_into_dictionary_words.py',
      'string_decompositions_into_dictionary_words.tsv', find_all_substrings))
