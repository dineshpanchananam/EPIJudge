from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/fibonacci.py
def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    return -1

=======
def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a
>>>>>>> d6b480a... more solved:epi_judge_python/done/fibonacci.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
