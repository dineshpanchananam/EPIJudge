from typing import List

from test_framework import generic_test
from functools import lru_cache

def is_pal(a):
  return a == a[::-1]

def palindrome_decompositions(text: str) -> List[List[str]]:
  # n = len(text)
  # ans = []
  # for i in range(n):
  #   sbstr = text[:i+1]
  #   if is_pal(sbstr):
  #     sub = palindrome_decompositions(text[i+1:]) or [[]]
  #     ans.extend([[sbstr]+x for x in sub])
  # return ans

  @lru_cache
  def helper(i, j):
    if i > j:
      return []
    res = []
    for k in range(i, j+1):
      s = text[i:k+1]
      if is_pal(s):
        sub = helper(k+1, j) or [[]]
        res.extend([[s]+x for x in sub])
    return res

  n = len(text)
  return helper(0, n-1)

def comp(a, b):
  return sorted(a) == sorted(b)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('enumerate_palindromic_decompositions.py',
                                   'enumerate_palindromic_decompositions.tsv',
                                   palindrome_decompositions, comp))
