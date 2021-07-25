from test_framework import generic_test

def can_form_palindrome(s: str) -> bool:
  from collections import Counter
  return sum(1 for x in Counter(s).values() if x%2 == 1) <= 1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_string_permutable_to_palindrome.py',
                                   'is_string_permutable_to_palindrome.tsv',
                                   can_form_palindrome))
