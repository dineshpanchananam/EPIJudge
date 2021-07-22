from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def remove_duplicates(L: ListNode) -> Optional[ListNode]:
  new_list = c = ListNode(7777)
  while L:
    if c.data != L.data:
      c.next = L
      c = c.next
    L = L.next
  c.next = None
  return new_list.next

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('remove_duplicates_from_sorted_list.py',
                                   'remove_duplicates_from_sorted_list.tsv',
                                   remove_duplicates))
