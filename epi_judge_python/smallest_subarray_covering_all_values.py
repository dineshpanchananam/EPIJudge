import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(
  paragraph: List[str],
  keywords: List[str],
) -> Subarray:
  n, m = len(paragraph), len(keywords)
  ptr, k = 0, 0
  x, y = 0, n
  pos_map = {}
  pos = [float('inf')]*m
  for i in range(n):-
    pos_map[paragraph[i]] = i
    if paragraph[i] == keywords[ptr]:
      ptr += 1
    if ptr == m:
      last_occ_first_kw = pos_map[keywords[0]]
      if y-x+1 > i-last_occ_first_kw+1:
        x, y = last_occ_first_kw, i
      ptr = 0

  print(f"returning {paragraph[x:y+1]}")
  return Subarray(x, y)

@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
  result = executor.run(
    functools.partial(find_smallest_sequentially_covering_subset, paragraph,
                      keywords))

  kw_idx = 0
  para_idx = result.start
  if para_idx < 0:
    raise RuntimeError('Subarray start index is negative')

  while kw_idx < len(keywords):
    if para_idx >= len(paragraph):
      raise TestFailure('Not all keywords are in the generated subarray')
    if para_idx >= len(paragraph):
      raise TestFailure('Subarray end index exceeds array size')
    if paragraph[para_idx] == keywords[kw_idx]:
      kw_idx += 1
    para_idx += 1

  return result.end-result.start+1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'smallest_subarray_covering_all_values.py',
      'smallest_subarray_covering_all_values.tsv',
      find_smallest_sequentially_covering_subset_wrapper))
