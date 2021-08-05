from typing import Set
import collections
import string
from test_framework import generic_test

def dist(s, t):
  if len(s) != len(t):
    return -1
  return sum(1 for i in range(len(s)) if s[i] != t[i])

def transform_string(D: Set[str], s: str, t: str) -> int:
  q = collections.deque([(s, 0)])
  D.remove(s)
  while q:
    word, dst = q.popleft()
    if word == t:
      return dst
    for k in range(len(word)):
      l, r = word[:k], word[k+1:]
      for kth in string.ascii_lowercase:
        nxt = l+kth+r
        if nxt in D:
          D.remove(nxt)
          q.append((nxt, dst+1))
  return -1

if __name__ == '__main__':
  # print(
  #   transform_string(
  #     {"bat", "cat", "cot", "dog", "dag", "dot"},
  #     "cat",
  #     "dog",
  #   ))
  exit(
    generic_test.generic_test_main('string_transformability.py',
                                   'string_transformability.tsv',
                                   transform_string))
