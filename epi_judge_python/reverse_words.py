import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].

def reverse_between(a, i, j):
  for k in range((j-i+1)//2):
    a[i+k], a[j-k] = a[j-k], a[i+k]

def reverse_words(s):
  i = 0
  j = 0
  n = len(s)
  while i < n:
    while i < n and s[i] == ' ':
      i += 1
    j = i
    while j < n and s[j] != ' ':
      j += 1
    reverse_between(s, i, j-1)
    i = j

  s.reverse()

@enable_executor_hook
def reverse_words_wrapper(executor, s):
  s_copy = list(s)

  executor.run(functools.partial(reverse_words, s_copy))

  return ''.join(s_copy)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                   reverse_words_wrapper))
