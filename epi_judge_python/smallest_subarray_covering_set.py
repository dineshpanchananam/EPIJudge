import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

  j = 0
  word_count = collections.defaultdict(int)
  ans = [0, float('inf')]
  for i in range(len(paragraph)):
    word = paragraph[i]
    if word in keywords:
      word_count[word] += 1

    while j <= i and len(keywords) == len(word_count):
      if ans[1]-ans[0]+1 > i-j+1:
        ans = [j, i]

      word_j = paragraph[j]
      if word_j in word_count:
        word_count[word_j] -= 1
        if not word_count[word_j]:
          del word_count[word_j]
      j += 1

  return Subarray(ans[0], ans[1])

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
  copy = keywords

  (start, end) = executor.run(
    functools.partial(find_smallest_subarray_covering_set, paragraph,
                      keywords))

  if (start < 0 or start >= len(paragraph) or end < 0 or end >= len(paragraph)
      or start > end):
    raise TestFailure('Index out of range')

  for i in range(start, end+1):
    copy.discard(paragraph[i])

  if copy:
    raise TestFailure('Not all keywords are in the range')

  return end-start+1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'smallest_subarray_covering_set.py',
      'smallest_subarray_covering_set.tsv',
      find_smallest_subarray_covering_set_wrapper))
