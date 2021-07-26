from test_framework import generic_test
from math import log

def is_palindrome_number(x: int) -> bool:
  y, z = 0, abs(x)
  while z:
    y = y*10+z%10
    z //= 10
  return x == y

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_number_palindromic.py',
                                   'is_number_palindromic.tsv',
                                   is_palindrome_number))
