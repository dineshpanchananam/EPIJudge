from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
  e = ep = ListNode()
  o = op = ListNode()
  i = 0
  while L:
    if not i:
      ep.next = L
      ep = ep.next
    else:
      op.next = L
      op = op.next
    i ^= 1
    L = L.next
  op.next = None
  ep.next = o.next
  return e.next


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('even_odd_list_merge.py',
                                   'even_odd_list_merge.tsv', even_odd_merge))
