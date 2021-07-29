from typing import Iterator, List

from test_framework import generic_test
import heapq as h

def print_mx_heap(heap: 'MaxHeap'):
  return sorted([-x for x in heap._max_h])

class MaxHeap:
  def __init__(self):
    self._max_h = []
    h.heapify(self._max_h)

  def push(self, value):
    h.heappush(self._max_h, -value)

  def pop(self):
    heap = self._max_h
    if heap:
      return -h.heappop(heap)

  def max(self):
    return -self._max_h[0]

  def empty(self):
    return self.len() == 0

  def len(self):
    return len(self._max_h)

def online_median(sequence: Iterator[int]) -> List[float]:
  mx_hp, mn_hp = MaxHeap(), []
  medians = []
  for n, s in enumerate(sequence, 1):
    if not mn_hp or s >= mn_hp[0]:
      h.heappush(mn_hp, s)
    else:
      mx_hp.push(s)

    while not mx_hp.empty() and mn_hp and mn_hp[0] < mx_hp.max():
      mx_hp.push(h.heappop(mn_hp))

    if mx_hp.len() > len(mn_hp)+1:
      h.heappush(mn_hp, mx_hp.pop())
    elif len(mn_hp) > mx_hp.len():
      mx_hp.push(h.heappop(mn_hp))

    medians.append(mx_hp.max()/1.0 if n & 1 else (mx_hp.max()+mn_hp[0])/2.0)
  return medians

  # print()
  # m, n = 0, 0
  # for x in sequence:
  #   print(f"pushing {x}")
  #   if mx_hp.empty():
  #     mx_hp.push(x)
  #   elif not mn_hp:
  #     mn_hp.append(x)
  #   else:
  #     if x >= mn_hp[0]:
  #       h.heappush(mn_hp, x)
  #     else:
  #       mx_hp.push(x)

  #   while mn_hp and mn_hp[0] < mx_hp.max():
  #     mx_hp.push(mn_hp.pop())

  #   m, n = mx_hp.len(), len(mn_hp)
  #   for i in range(max(0, n-m)):
  #     mx_hp.push(h.heappop(mn_hp))
  #   for i in range(max(0, m-n-1)):
  #     h.heappush(mn_hp, mx_hp.pop())

  #   print(print_mx_heap(mx_hp._max_h), " [ -- ] ", mn_hp)
  #   m, n = mx_hp.len(), len(mn_hp)
  #   if (m+n) & 1:
  #     medians.append(mx_hp.max()/1.0)
  #   else:
  #     medians.append((mx_hp.max()+mn_hp[0])/2.0)
  #   print(medians)
  # return medians

def online_median_wrapper(sequence):
  return online_median(iter(sequence))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                   online_median_wrapper))
