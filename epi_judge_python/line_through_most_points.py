import collections
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Point = collections.namedtuple('Point', ('x', 'y'))

def find_line_with_most_points(points: List[Point]) -> int:
  res = 0
  for i, p1 in enumerate(points):
    slope_table = collections.defaultdict(int)
    overlap_points = 1
    for p2 in points[i+1:]:
      if p1 == p2:
        overlap_points += 1
      elif p1.x == p2.x:
        slope_table[(0, 1)] += 1
      else:
        xdiff = p2.x-p1.x
        ydiff = p2.y-p1.y
        gcd = math.gcd(ydiff, xdiff)
        xdiff, ydiff = xdiff//gcd, ydiff//gcd
        if xdiff < 0:
          xdiff, ydiff = -xdiff, -ydiff
        slope_table[(xdiff, ydiff)] += 1
    res = max(
      res,
      max(slope_table.values(), default=0)+overlap_points,
    )
  return res

@enable_executor_hook
def find_line_with_most_points_wrapper(executor, points):
  points = [Point(*x) for x in points]
  return executor.run(functools.partial(find_line_with_most_points, points))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('line_through_most_points.py',
                                   'line_through_most_points.tsv',
                                   find_line_with_most_points_wrapper))
