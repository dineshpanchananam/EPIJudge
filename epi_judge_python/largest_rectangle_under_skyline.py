from typing import List

from test_framework import generic_test

# 2 1 3 4 5 2
def calculate_largest_rectangle(a: List[int]) -> int:
  st, area = [], 0
  for i, h in enumerate(a+[0]):
    while st and a[st[-1]] >= h:
      hgt = a[st.pop()]
      wid = i if not st else i-st[-1]-1
      area = max(area, hgt*wid)
    st.append(i)
  return area
  # area = a[0] if a else 0
  # n = len(a)
  # for i in range(n-1):
  #   min_so_far = a[i]
  #   for j in range(i+1, n):
  #     min_so_far = min(a[j], min_so_far)
  #     area = max(area, (j-i+1)*min_so_far)
  # return area

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                   'largest_rectangle_under_skyline.tsv',
                                   calculate_largest_rectangle))
