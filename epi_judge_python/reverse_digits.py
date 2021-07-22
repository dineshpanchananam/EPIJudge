from test_framework import generic_test

def reverse(x: int) -> int:
  y = 0
  x, signed = (x, False) if x >= 0 else (abs(x), True)
  while x:
    x, y = x//10, y*10+(x%10)
  return -y if signed else y

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('reverse_digits.py', 'reverse_digits.tsv',
                                   reverse))
