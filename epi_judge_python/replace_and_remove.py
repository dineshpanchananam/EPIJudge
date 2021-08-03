import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def replace_and_remove(size: int, s: List[str]) -> int:
  last = len(s)-1
  for i in range(size-1, -1, -1):
    if s[i] == "a":
      s[last] = s[last-1] = 'd'
      last -= 2
    elif s[i] != "b":
      s[last] = s[i]
      last -= 1

  k = 0
  last += 1
  while last < len(s):
    s[k] = s[last]
    k, last = k+1, last+1
  return k

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
  res_size = executor.run(functools.partial(replace_and_remove, size, s))
  return s[:res_size]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('replace_and_remove.py',
                                   'replace_and_remove.tsv',
                                   replace_and_remove_wrapper))
