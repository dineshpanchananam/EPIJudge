from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/gcd.py
def gcd(x: int, y: int) -> int:
    # TODO - you fill in here.
    return 0
=======
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
>>>>>>> cf3ad5a... solved some:epi_judge_python/done/gcd.py


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
