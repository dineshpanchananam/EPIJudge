from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from functools import reduce

<<<<<<< HEAD:epi_judge_python/absent_value_array.py
def find_missing_element(stream: Iterator[int]) -> int:
    # TODO - you fill in here.
    return 0

=======
def find_missing_element(stream):
	maxm, xor = 0, 0
	ls = set()
	for i in stream:
		maxm = max(maxm, i)
		ls.add(i)
	for i in range(maxm+1):
		if i not in ls:
			return i
>>>>>>> 7212bde... 12.29:epi_judge_python/absent_value_array.wip.py

def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
