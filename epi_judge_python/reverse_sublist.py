from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    c = dummy = ListNode()
    for i in range(start - 1):
        c.next = L
        c = c.next
        L = L.next

    tmp = None
    for i in range(start, finish + 1):
        if L:
            l_next = L.next
            L.next = tmp
            tmp = L
            L = l_next

    c.next = tmp
    while c.next:
        c = c.next
    c.next = L
    return dummy.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
