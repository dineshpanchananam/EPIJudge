from test_framework import generic_test
import math


def is_palindrome_number(x: int) -> bool:
    if x < 1:
        return x == 0
    num_digits = math.log10(x) + 1
    msd_mask = 100 ** (num_digits - 1)

    # y, r = x, 0
    # while y:
    #     r = r * 10 + (y % 10)
    #     y //= 10
    # return r == x


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_number_palindromic.py",
            "is_number_palindromic.tsv",
            is_palindrome_number,
        )
    )
