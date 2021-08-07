from test_framework import generic_test
from functools import lru_cache

@lru_cache
def get_height(cases: int, drops: int) -> int:
  if drops == 0 or cases == 0:
    return 0
  if cases == 1:
    return drops
  return get_height(cases, drops-1)+1+get_height(cases-1, drops-1)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_safe_height.py', 'max_safe_height.tsv',
                                   get_height))
