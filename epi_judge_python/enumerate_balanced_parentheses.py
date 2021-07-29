from typing import List

from test_framework import generic_test, test_utils

def generate_balanced_parentheses(n: int) -> List[str]:
  def back(opened=0, closed=0):
    if opened+closed == 2*n and opened == closed:
      pairs.append(''.join(tmp))
      return
    if opened > n or closed > opened:
      return

    for brac, o, c in [('(', 1, 0), (')', 0, 1)]:
      tmp.append(brac)
      back(opened+o, closed+c)
      tmp.pop()

  pairs, tmp = [], []
  back()
  return pairs

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                   'enumerate_balanced_parentheses.tsv',
                                   generate_balanced_parentheses,
                                   test_utils.unordered_compare))
