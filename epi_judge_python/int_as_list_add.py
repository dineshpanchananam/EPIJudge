from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
    l3 = l4 = ListNode()
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.data
            l1 = l1.next
        if l2:
            carry += l2.data
            l2 = l2.next
        l3.next = ListNode(carry % 10)
        l3 = l3.next
        carry //= 10

    return l4.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_list_add.py", "int_as_list_add.tsv", add_two_numbers
        )
    )
