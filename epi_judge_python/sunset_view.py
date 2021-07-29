from typing import Iterator, List

from test_framework import generic_test

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
  can_see = []
  for i, h in enumerate(sequence):
    while can_see and h >= can_see[-1][-1]:
      can_see.pop()
    can_see.append([i, h])
  return [x[0] for x in reversed(can_see)]

def examine_buildings_with_sunset_wrapper(sequence):
  return examine_buildings_with_sunset(iter(sequence))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                   examine_buildings_with_sunset))
