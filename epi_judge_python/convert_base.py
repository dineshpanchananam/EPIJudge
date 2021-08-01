from test_framework import generic_test
import string as s
from functools import reduce

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
  signed = num_as_string[0] == '-'
  value = reduce(lambda x, y: x*b1+s.hexdigits.index(y.lower()),
                 num_as_string[signed:], 0)

  str2 = ''
  while value:
    str2 = f"{s.hexdigits[value%b2]}{str2}"
    value //= b2

  return f"{'-' if signed else ''}{str2}".upper() or '0'

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                   convert_base))
