from typing import Iterator, List

from test_framework import generic_test
import heapq as h

def online_median(sequence: Iterator[int]) -> List[float]:
  mx_hp, mn_hp = [], []
  medians = []
  for n, s in enumerate(sequence, 1):
    h.heappush(mx_hp, -h.heappushpop(mn_hp, s))
    if len(mx_hp) > len(mn_hp):
      h.heappush(mn_hp, -h.heappop(mx_hp))
    medians.append(mn_hp[0] if n & 1 else (mn_hp[0]-mx_hp[0])/2.0)
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
