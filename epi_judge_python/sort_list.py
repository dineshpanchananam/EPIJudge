from typing import Optional

from list_node import ListNode
from sorted_lists_merge import merge_two_sorted_lists
from test_framework import generic_test

def stable_sort_list(L: ListNode) -> Optional[ListNode]:
  if L and L.next:
    slow, fst = L, L
    while fst and fst.next:
      fst = fst.next.next
      if fst: slow = slow.next
    slow_next = slow.next
    slow.next = None
    return merge_two_sorted_lists(
      stable_sort_list(L),
      stable_sort_list(slow_next),
    )

  return L

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                   stable_sort_list))
