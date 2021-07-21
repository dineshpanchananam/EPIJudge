from test_framework import generic_test

def is_palindromic(s: str) -> bool:
  return s == s[::-1]
  # n = len(s)
  # for i in range(n//2):
  #   if s[i] != s[n-1-i]:
  #     return False
  # return True

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_string_palindromic.py',
                                   'is_string_palindromic.tsv',
                                   is_palindromic))
