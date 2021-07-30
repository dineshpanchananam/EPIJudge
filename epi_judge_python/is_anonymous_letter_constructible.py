from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:

  l, m = Counter(letter_text), Counter(magazine_text)
  return all(c in m and m[c] >= f for c, f in l.items())

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_anonymous_letter_constructible.py',
                                   'is_anonymous_letter_constructible.tsv',
                                   is_letter_constructible_from_magazine))
