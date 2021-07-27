from test_framework import generic_test

def multiply(x: int, y: int) -> int:
  k = 0
  while 2*k <= y:
    y -= 2*k
    k *= 2

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('primitive_multiply.py',
                                   'primitive_multiply.tsv', multiply))
