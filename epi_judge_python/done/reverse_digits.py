from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/reverse_digits.py
def reverse(x: int) -> int:
    # TODO - you fill in here.
    return 0
=======
def reverse(x):
  sign, x = bool(x < 0), abs(x)
  ans = 0
  while x:
    x, rem = divmod(x, 10)
    ans = ans * 10 + rem
  return -ans if sign else ans 
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/reverse_digits.py


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
