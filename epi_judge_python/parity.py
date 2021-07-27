from test_framework import generic_test

def parity(x: int) -> int:
  for i in range(5, -1, -1):
    x ^= x >> (1 << i)
  return x & 1

if __name__ == '__main__':
  exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
