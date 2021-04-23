from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    p1 = L
    for _ in range(k):
        p1 = p1.next
    if not p1:
        return L.next

    p2 = L
    while p1 and p1.next:
        p1 = p1.next
        p2 = p2.next
    if p2 and p2.next:
        p2.next = p2.next.next
    return L


# a b c

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
