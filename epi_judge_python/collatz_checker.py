from test_framework import generic_test

def test_collatz_conjecture(n: int) -> bool:
  s = {1}
  while n not in s:
    s.add(n)
    n = n//2 if n%2 == 0 else 3*n+1
  return n == 1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('collatz_checker.py', 'collatz_checker.tsv',
                                   test_collatz_conjecture))
