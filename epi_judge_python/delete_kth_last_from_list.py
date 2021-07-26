from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
  a, b = L, L
  for i in range(k):
    b = b.next
  prev = None
  while b:
    prev, a, b = a, a.next, b.next
  if not prev:
    return L.next
  prev.next = prev.next.next
  return L

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('delete_kth_last_from_list.py',
                                   'delete_kth_last_from_list.tsv',
                                   remove_kth_last))
