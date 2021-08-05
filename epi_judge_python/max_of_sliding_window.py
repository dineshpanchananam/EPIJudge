import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import collections
from queue_with_max import QueueWithMax

class TrafficElement:
  def __init__(self, time: int, volume: float) -> None:
    self.time = time
    self.volume = volume

  def __lt__(self, other):
    return self.volume < other.volume

def calculate_traffic_volumes(A: List[TrafficElement],
                              w: int) -> List[TrafficElement]:
  # result = []
  # q = QueueWithMax()
  # for t in A:
  #   q.enqueue(t)
  #   while t.time-q.max().time > w:
  #     q.dequeue()
  #   result.append(TrafficElement(t.time, q.max().volume))
  # return result

  q = collections.deque()
  result = []
  for t in A:
    while q and q[-1].volume < t.volume:
      q.pop()
    q.append(t)
    while t.time-q[0].time > w:
      q.popleft()
    result.append(TrafficElement(t.time, q[0].volume))
  return result

@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
  A = [TrafficElement(t, v) for (t, v) in A]

  result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

  return [(x.time, x.volume) for x in result]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_of_sliding_window.py',
                                   'max_of_sliding_window.tsv',
                                   calculate_traffic_volumes_wrapper))
