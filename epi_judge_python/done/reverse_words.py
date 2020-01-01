import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


<<<<<<< HEAD:epi_judge_python/reverse_words.py
# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
=======
def rev(s, i, j):
  mid = (j - i + 1) // 2
  for k in range(mid):
    s[i+k], s[j-k] = s[j-k], s[i+k]

# Assume s is a string encoded as bytearray.
>>>>>>> ee84769... added run and check:epi_judge_python/done/reverse_words.py
def reverse_words(s):
  start, size = 0, len(s)
  rev(s, start, size-1)
  while start < size:
    # it's a space, ignore
    if s[start] == 32:
      start += 1
      continue
    word = start
    while word < size and s[word] != 32:
      word += 1
    rev(s, start, word-1)
    start = word

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
