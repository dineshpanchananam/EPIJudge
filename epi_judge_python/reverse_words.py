import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse(a, i, j):
    while i < j:
        a[i], a[j] = a[j], a[i]
        i, j = i + 1, j - 1


def reverse_words(s):
    n = len(s)
    reverse(s, 0, n - 1)
    i = 0
    while i < n:
        if s[i] != " ":
            j = i
            while j < n and s[j] != " ":
                j += 1
            reverse(s, i, j - 1)
            i = j - 1
        i += 1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
