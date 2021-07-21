from test_framework import generic_test
from test_framework.test_failure import TestFailure

def decoding(s: str) -> str:
  ans = ''
  x, f = '', 0
  for c in s:
    if c.isdigit():
      f = f*10+int(c)
    else:
      ans += c*f
      f = 0
  return ans

def encoding(s: str) -> str:
  code = ''
  f, c = 0, ""
  for x in s:
    if c == x:
      f += 1
      continue
    code += f"{f}{c}"
    c, f = x, 1
  return (code+f"{f}{x}")[1:]

def rle_tester(encoded, decoded):
  if decoding(encoded) != decoded:
    raise TestFailure('Decoding failed')
  if encoding(decoded) != encoded:
    raise TestFailure('Encoding failed')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('run_length_compression.py',
                                   'run_length_compression.tsv', rle_tester))
