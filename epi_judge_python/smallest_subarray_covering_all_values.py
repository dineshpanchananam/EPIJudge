import collections
import functools
import bisect
from typing import List
from test_framework.test_failure import TestFailure
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from test_framework.test_failure import TestFailure

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(
  paragraph: List[str],
  keywords: List[str],
) -> Subarray:
  ans = [0, len(paragraph)]
  kw_idx = {k: i for i, k in enumerate(keywords)}
  inf = float('inf')
  shortest = inf
  n = len(kw_idx)
  last_seen = [-1]*n
  short_path = [inf]*n
  for i, w in enumerate(paragraph):
    if w in kw_idx:
      idx = kw_idx[w]
      if idx == 0:
        short_path[idx] = 1
      elif short_path[idx-1] != inf:
        short_path[idx] = short_path[idx-1]+i-last_seen[idx-1]
      last_seen[idx] = i
      if idx == n-1 and shortest > short_path[-1]:
        shortest = short_path[-1]
        ans = [i-shortest+1, i]

  return Subarray(*ans)

  # ans = (float('-inf'), float('inf'))
  # w_to_i = collections.defaultdict(list)
  # kw = set(keywords)
  # for i, w in enumerate(paragraph):
  #   if w in kw:
  #     w_to_i[w] += i,
  # starts = w_to_i[keywords[0]]
  # for s in starts:
  #   s1 = s
  #   chain = 1
  #   for k in keywords[1:]:
  #     idx = bisect.bisect(w_to_i[k], s)
  #     if len(w_to_i[k]) == idx:
  #       break
  #     s = w_to_i[k][idx]
  #     chain += 1

  #   if chain == len(keywords):
  #     if ans[1]-ans[0] > s-s1:
  #       ans = [s1, s]

  #   if ans[1]-ans[0]+1 == len(keywords):
  #     break

  # return Subarray(ans[0], ans[1])

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
