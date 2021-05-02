from test_framework import generic_test
from collections import Counter
from string import punctuation


def is_palindrome(s: str) -> bool:
    s = [x for x in s if x in punctuation]
    return sum(1 for x in Counter(s).values() if x & 1) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
