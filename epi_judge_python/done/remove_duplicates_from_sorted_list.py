from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode

<<<<<<< HEAD:epi_judge_python/remove_duplicates_from_sorted_list.py
def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None

=======
def remove_duplicates(L):
  head = tail = ListNode('dummy')
  while L:
    if tail.data != L.data:
      tail.next = L
      tail = L
    L = L.next
  tail.next = None
  return head.next
  
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/remove_duplicates_from_sorted_list.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
