from test_framework import generic_test
from test_framework.test_failure import TestFailure

def int_to_string(x: int) -> str:
  signed = x < 0
  x = abs(x)
  string = ["0"] if x == 0 else []
  while x:
    string.append(chr(48+x%10))
    x //= 10
  string = "".join(reversed(string))
  return f"-{string}" if signed else string

def string_to_int(s: str) -> int:
  signed = s[0] == '-'
  plus = s[0] == '+'
  num = 0
  for i in s[1 if (plus or signed) else 0:]:
    num = num*10+ord(i)-48
  return -num if signed else num

def wrapper(x, s):
  if int(int_to_string(x)) != x:
    raise TestFailure('Int to string conversion failed')
  if string_to_int(s) != x:
    raise TestFailure('String to int conversion failed')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('string_integer_interconversion.py',
                                   'string_integer_interconversion.tsv',
                                   wrapper))
