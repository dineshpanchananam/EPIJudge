from typing import List

from test_framework import generic_test

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
  c = image[x][y]
  m, n = len(image), len(image[0])
  st = [(x, y)]
  while st:
    i, j = st.pop()
    if 0 <= i < m and 0 <= j < n and image[i][j] == c:
      image[i][j] = 1-c
      st.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

def flip_color_wrapper(x, y, image):
  flip_color(x, y, image)
  return image

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('matrix_connected_regions.py',
                                   'painting.tsv', flip_color_wrapper))
