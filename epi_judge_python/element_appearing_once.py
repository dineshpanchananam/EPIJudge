from typing import List

from test_framework import generic_test
from functools import reduce

<<<<<<< HEAD
def find_element_appears_once(A: List[int]) -> int:
    # TODO - you fill in here.
    return 0

=======
def find_element_appears_once(A):
  # hint:
>>>>>>> 6e7e48e... some wip

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('element_appearing_once.py',
                                       'element_appearing_once.tsv',
                                       find_element_appears_once))
