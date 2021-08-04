import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple("Endpoint", ("time", "is_start"))

def find_max_simultaneous_events(A: List[Event]) -> int:
  size = max(x.finish for x in A)
  d = [0]*(size+2)
  for e in A:
    d[e.start] += 1
    d[e.finish+1] -= 1
  for i in range(1, size+1):
    d[i] += d[i-1]
  return max(d)

  # events = [
  #   p for e in A for p in (
  #     Endpoint(e.start, True),
  #     Endpoint(e.finish, False),
  #   )
  # ]
  # events.sort(key=lambda x: (x.time, not x.is_start))
  # max_evts, sim_evts = 0, 0
  # for e in events:
  #   if e.is_start:
  #     sim_evts += 1
  #     max_evts = max(max_evts, sim_evts)
  #   else:
  #     sim_evts -= 1
  # return max_evts

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
  events = [Event(*x) for x in events]
  return executor.run(functools.partial(find_max_simultaneous_events, events))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('calendar_rendering.py',
                                   'calendar_rendering.tsv',
                                   find_max_simultaneous_events_wrapper))
