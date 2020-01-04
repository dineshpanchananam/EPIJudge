from test_framework import generic_test

# 1 2 3 4 5
# 1 3 2 5 4

<<<<<<< HEAD:epi_judge_python/snake_string.py
def snake_string(s: str) -> str:
    # TODO - you fill in here.
    return ''
=======
def snake_string(s):
  return s[1::4] + s[::2] + s[3::4]
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/snake_string.py


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
