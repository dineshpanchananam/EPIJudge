from test_framework import generic_test

def reverse(x: int) -> int:
  signed = x < 0
  x, y = abs(x), 0
  while x:
    d, r = divmod(x, 10)
    x, y = d, 10*y+r
  return -y if signed else y

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("reverse_digits.py", "reverse_digits.tsv",
                                   reverse))
