from test_framework import generic_test
from test_framework.test_failure import TestFailure


<<<<<<< HEAD:epi_judge_python/run_length_compression.py
def decoding(s: str) -> str:
    # TODO - you fill in here.
    return ''


def encoding(s: str) -> str:
    # TODO - you fill in here.
    return ''
=======
def decoding(s):
  f = ''
  ans = []
  for c in s:
    if c.isdigit():
      f += c
    elif f:
      ans.append(c * int(f))
      f = ''
  return ''.join(ans)

def encoding(s):
  s += '0'
  ans = []
  curr, f = None, 0
  for c in s:
    if curr != c:
      if curr:
        ans.extend([str(f), curr])
      curr, f = c, 1
    else:
      f += 1
  return ''.join(ans)
>>>>>>> 7212bde... 12.29:epi_judge_python/done/run_length_compression.py


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
