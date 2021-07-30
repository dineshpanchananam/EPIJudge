import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
  for i in range(len(A)):
    while A[i] != A[A[i]]:
      tmp = A[i]
      A[i] = A[A[i]]
      A[tmp] = tmp
  for i in range(len(A)):
    if A[i] != i:
      return DuplicateAndMissing(A[i], i)

def res_printer(prop, value):
  def fmt(x):
    return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

  return fmt(value) if prop in (PropertyName.EXPECTED,
                                PropertyName.RESULT) else value

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('search_for_missing_element.py',
                                   'find_missing_and_duplicate.tsv',
                                   find_duplicate_missing,
                                   res_printer=res_printer))
