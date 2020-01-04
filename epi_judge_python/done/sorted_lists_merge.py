from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode

<<<<<<< HEAD:epi_judge_python/sorted_lists_merge.py
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None


=======
def merge_two_sorted_lists(L1, L2):
  head = curr = ListNode()
  while L1 and L2:
    if L1.data < L2.data:
      curr.next, L1 = L1, L1.next
    else:
      curr.next, L2 = L2, L2.next
    curr = curr.next
  curr.next = L1 or L2
  return head.next
    
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/sorted_lists_merge.py
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
