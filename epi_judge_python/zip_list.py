from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def reverse(l):
  rev = None
  while l:
    l_next = l.next
    l.next = rev
    rev, l = l, l_next
  return rev

def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
  s, f = L, L
  while f and f.next:
    f = f.next.next
    s = s.next
  s_next = s.next
  s.next, s = None, s_next
  s = reverse(s)
  l = c = ListNode()
  while L and s:
    c.next, L = L, L.next
    c.next.next, s = s, s.next
    c = c.next.next
  c.next = L or s
  return l.next

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                   zipping_linked_list))
