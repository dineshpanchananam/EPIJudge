from typing import List

from test_framework import generic_test, test_utils


def backtrack(A, ans, tmp):
    if len(tmp) == len(A):
        ans.append(tmp)
        return
    for x in A:
        if x not in tmp:
            backtrack(A, ans, tmp + [x])


def permutations(A: List[int]) -> List[List[int]]:
    ans = []
    backtrack(A, ans, [])
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
