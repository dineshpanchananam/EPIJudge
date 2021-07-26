from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
  carry = 0
  L3 = c = ListNode(data=-1)
  while L1 or L2 or carry:
    l1, L1 = (L1.data, L1.next) if L1 else (0, None)
    l2, L2 = (L2.data, L2.next) if L2 else (0, None)
    carry += l1+l2
    c.next = ListNode(carry%10)
    c = c.next
    carry //= 10

  return L3.next

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('int_as_list_add.py', 'int_as_list_add.tsv',
                                   add_two_numbers))
