from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def rev(s):
  new = None
  while s:
    s_next = s.next
    s.next = new
    new, s = s, s_next
  return new

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

  if not L or (finish == start):
    return L

  # TODO - you fill in here.
  L = ListNode(next=L)
  s, f, prev = L, L, None
  for i in range(start):
    prev, s = s, s.next
  for i in range(finish):
    f = f.next
  f_next = f.next
  f.next = None
  prev.next = rev(s)
  s.next = f_next
  return L.next

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('reverse_sublist.py', 'reverse_sublist.tsv',
                                   reverse_sublist))
