from typing import List

from test_framework import generic_test

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
  s = set()
  j, ans = 0, 0
  for i in range(len(A)):
    if A[i] not in s:
      s.add(A[i])
      ans = max(ans, i-j+1)
      continue

    while j < i and A[j] != A[i]:
      s.remove(A[j])
      j += 1
    j += 1

  return max(ans, len(A)-j)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'longest_subarray_with_distinct_values.py',
      'longest_subarray_with_distinct_values.tsv',
      longest_subarray_with_distinct_entries))
