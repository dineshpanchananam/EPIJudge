from typing import List

from test_framework import generic_test

def generate_pascal_triangle(n: int) -> List[List[int]]:
  if not n:
    return []
  tri = [[1]]
  for i in range(n-1):
    new, last = [1], tri[-1]
    for k in range(1, len(last)):
      new.append(last[k-1]+last[k])
    new.append(1)
    tri.append(new)
  return tri

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('pascal_triangle.py', 'pascal_triangle.tsv',
                                   generate_pascal_triangle))
