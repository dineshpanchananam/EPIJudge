from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
  turn = 1
  evens = e_ptr = ListNode()
  odds = o_ptr = ListNode()
  while L:
    if turn:
      e_ptr.next = L
      e_ptr = e_ptr.next
    else:
      o_ptr.next = L
      o_ptr = o_ptr.next
    turn ^= 1
    L = L.next

  o_ptr.next = None
  e_ptr.next = odds.next
  return evens.next

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('even_odd_list_merge.py',
                                   'even_odd_list_merge.tsv', even_odd_merge))
