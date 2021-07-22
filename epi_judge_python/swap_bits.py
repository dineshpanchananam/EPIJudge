from test_framework import generic_test

def swap_bits(x, i, j):
  for i in range(i, j+1):
    x ^= (1 << i)
  return x

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv', swap_bits))
