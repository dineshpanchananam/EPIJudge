from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def length(l):
  count = 0
  while l:
    count += 1
    l = l.next
  return count


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
  if not L:
    return

  k %= length(L)
  if not k:
    return L

  p1, p2 = L, L
  for i in range(k):
    p2 = p2.next
  while p2.next:
    p1 = p1.next
    p2 = p2.next
  head = p1.next
  p1.next = None
  p2.next = L
  return head


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('list_cyclic_right_shift.py',
                                   'list_cyclic_right_shift.tsv',
                                   cyclically_right_shift_list))
