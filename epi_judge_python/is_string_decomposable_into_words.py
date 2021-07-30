import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from functools import lru_cache

def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:

  n = len(domain)
  words = {0: 0}

  for i in range(n):
    if i in words:
      for word in dictionary:
        k = len(word)
        if k and domain[i:i+k] == word:
          words[i+k] = (word, i)

  ans, start = [], n
  while start and start in words:
    ans.append(words[start][0])
    start = words[start][1]

  return ans[::-1]

# @lru_cache
# def helper(k):
#   for word in dictionary:
#     if word and word == domain[k:k+len(word)]:
#       offset = k+len(word)
#       if offset == n:
#         return [word]
#       if sub := helper(offset):
#         return [word]+sub
#   return []

# n = len(domain)
# return helper(0)

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
  result = executor.run(
    functools.partial(decompose_into_dictionary_words, domain, dictionary))

  if not decomposable:
    if result:
      raise TestFailure('domain is not decomposable')
    return

  if any(s not in dictionary for s in result):
    raise TestFailure('Result uses words not in dictionary')

  if ''.join(result) != domain:
    raise TestFailure('Result is not composed into domain')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_string_decomposable_into_words.py',
                                   'is_string_decomposable_into_words.tsv',
                                   decompose_into_dictionary_words_wrapper))
