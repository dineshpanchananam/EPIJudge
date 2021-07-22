from test_framework import generic_test

def fibonacci(n: int) -> int:
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("fibonacci.py", "fibonacci.tsv", fibonacci))
