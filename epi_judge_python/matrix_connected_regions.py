from typing import List

from test_framework import generic_test

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
  pass

def flip_color_wrapper(x, y, image):
  flip_color(x, y, image)
  return image

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('matrix_connected_regions.py',
                                   'painting.tsv', flip_color_wrapper))
