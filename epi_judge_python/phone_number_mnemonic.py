from typing import List

from test_framework import generic_test, test_utils

def phone_mnemonic(phone_number: str) -> List[str]:
  m = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
  result = [[]]
  for c in phone_number:
    sol = []
    for p in result:
      for x in m[int(c)]:
        sol.append(p+[x])
    result = sol

  return list(map("".join, result))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('phone_number_mnemonic.py',
                                   'phone_number_mnemonic.tsv',
                                   phone_mnemonic,
                                   comparator=test_utils.unordered_compare))
