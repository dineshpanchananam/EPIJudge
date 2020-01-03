from typing import List

from test_framework import generic_test


<<<<<<< HEAD:epi_judge_python/pascal_triangle.py
def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
=======
def generate_pascal_triangle(n):
  if not n:
>>>>>>> c369a0b... some other problems:epi_judge_python/done/pascal_triangle.py
    return []
  trngle = [[1]]
  for _ in range(n-1):
    tmp, last = [], trngle[-1]
    for j in range(len(last)-1):
      tmp.append(last[j] + last[j+1])
    trngle.append([1] + tmp + [1])
  return trngle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
