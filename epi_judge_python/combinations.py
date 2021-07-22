from typing import List

from test_framework import generic_test, test_utils

def backtrack(n, k, ans, tmp):
  if k == 0:
    ans.append(tmp)
    return
  if n > 0:
    backtrack(n-1, k-1, ans, tmp+[n])
    backtrack(n-1, k, ans, tmp)

def combinations_1(n: int, k: int) -> List[List[int]]:
  ans = []
  backtrack(n, k, ans, [])
  return ans or [[]]

def combinations(n: int, k: int) -> List[List[int]]:
  if k == 0:
    return [[]]
  elif n == 0:
    return []

  return combinations(n-1, k)+[x+[n] for x in combinations(n-1, k-1)]

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main(
      "combinations.py",
      "combinations.tsv",
      combinations,
      comparator=test_utils.unordered_compare,
    ))
