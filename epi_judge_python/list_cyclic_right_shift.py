from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def length(l):
  size = 0
  while l:
    size += 1
    l = l.next
  return size

def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
  n = max(1, length(L))
  k %= n
  if not k:
    return L
  k = n-k
  kth, prev = L, None
  for i in range(k):
    prev, kth = kth, kth.next
  tail = kth
  while tail.next:
    tail = tail.next
  tail.next = L
  prev.next = None
  return kth

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('list_cyclic_right_shift.py',
                                   'list_cyclic_right_shift.tsv',
                                   cyclically_right_shift_list))
