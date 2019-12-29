from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/collatz_checker.py
def test_collatz_conjecture(n: int) -> bool:
    # TODO - you fill in here.
    return False

=======
def test_collatz_conjecture(n):
  seen = set([n])
  while n != 1:
    if n & 1:
      tmp = 3 * n + 1
      if tmp in seen:
        return False
      n = tmp
    else:
      n = n // 2
  return True
>>>>>>> cf3ad5a... solved some:epi_judge_python/done/collatz_checker.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
