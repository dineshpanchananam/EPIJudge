from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
  a = {1}
  while n not in a:
    a.add(n)
    n = 3*n+1 if n & 1 else n//2
  return n == 1


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('collatz_checker.py', 'collatz_checker.tsv',
                                   test_collatz_conjecture))
