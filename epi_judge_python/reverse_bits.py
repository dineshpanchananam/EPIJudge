from test_framework import generic_test

def reverse_bits(x: int) -> int:
  y = 0
  while x:
    y = (y << 1) | x & 1
    x >>= 1
  return y

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                   reverse_bits))
