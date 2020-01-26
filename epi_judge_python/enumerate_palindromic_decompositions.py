from typing import List

from test_framework import generic_test


<<<<<<< HEAD
def palindrome_decompositions(text: str) -> List[List[str]]:
    # TODO - you fill in here.
    return []
=======
def palindrome_decompositions(input):
  # TODO - you fill in here.
  return input
>>>>>>> 6e7e48e... some wip


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))