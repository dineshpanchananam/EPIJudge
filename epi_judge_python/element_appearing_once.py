from typing import List

from test_framework import generic_test

def find_element_appears_once(A: List[int]) -> int:
  bits = [0]*32
  for a in A:
    for i in range(32):
      if a < 0: bits[-1] += 1
      a = abs(a)
      bits[i] += a & 1
      a >>= 1
  value = sum(1 << i for (i, b) in enumerate(bits) if b%3 != 0)
  return 2**31-value if value >= 2**31 else value

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('element_appearing_once.py',
                                   'element_appearing_once.tsv',
                                   find_element_appears_once))
