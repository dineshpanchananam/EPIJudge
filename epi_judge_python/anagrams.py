from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    res = {}
    for word in dictionary:
        key = "".join(sorted(word))
        if key not in res:
            res[key] = []
        res[key].append(word)
    return [x for x in res.values() if len(x) > 1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare,
        )
    )
