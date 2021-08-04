import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

# gallons[i] is the amount of gas in city i, and
# distances[i] is the distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
  n = len(distances)
  ans = (0, 0)
  pairs = list(zip(gallons, distances))
  rem = 0
  for i in range(1, n):
    rem += gallons[i-1]-distances[i-1]//MPG
    if rem < ans[1]:
      ans = (i, rem)
  return ans[0]

  return 0

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
  result = executor.run(functools.partial(find_ample_city, gallons, distances))
  num_cities = len(gallons)
  tank = 0
  for i in range(num_cities):
    city = (result+i)%num_cities
    tank += gallons[city]*MPG-distances[city]
    if tank < 0:
      raise TestFailure('Out of gas on city {}'.format(i))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('refueling_schedule.py',
                                   'refueling_schedule.tsv',
                                   find_ample_city_wrapper))
