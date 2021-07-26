from test_framework import generic_test
import math

def square_root(x: float) -> float:
  l, h = [x, 1.0] if x < 1.0 else [1.0, x]
  while not math.isclose(l, h):
    m = (l+h)*0.5
    if m*m < x:
      l = m
    else:
      h = m
  return l

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('real_square_root.py',
                                   'real_square_root.tsv', square_root))
