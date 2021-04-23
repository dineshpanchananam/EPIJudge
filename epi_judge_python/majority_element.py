from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    el, freq = 0, 0
    for s in stream:
        if freq == 0:
            freq, el = 1, s
        elif el == s:
            freq += 1
        else:
            freq -= 1
    return el


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "majority_element.py", "majority_element.tsv", majority_search_wrapper
        )
    )
