from typing import List

from test_framework import generic_test, test_utils


def helper(A, idx, ans):
  if idx == len(A):
    ans.append(list(A))
  else:
    for i in range(idx, len(A)):
      A[i], A[idx] = A[idx], A[i]
      helper(A, idx+1, ans)
      A[i], A[idx] = A[idx], A[i]


def permutations(A: List[int]) -> List[List[int]]:
  ans = []
  helper(A, 0, ans)
  return ans


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main(
      "permutations.py",
      "permutations.tsv",
      permutations,
      test_utils.unordered_compare,
    ))
