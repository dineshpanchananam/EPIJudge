from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from sorted_lists_merge import merge_two_sorted_lists


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next:
        return L

    slow, fast = L, L
    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next
    right = slow.next
    slow.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(right))

    # # count sort
    # cache = {}
    # curr = L
    # while curr:
    #     if curr.data not in cache:
    #         cache[curr.data] = []
    #     cache[curr.data].append(curr)
    #     curr = curr.next

    # head = ListNode()
    # curr = head
    # for key in sorted(cache):
    #     for value in cache[key]:
    #         curr.next = value
    #         curr = value
    # curr.next = None
    # return head.next

    # # insertion sort
    # if not L or not L.next:
    #     return L

    # head = ListNode()
    # while L:
    #     L_next = L.next
    #     last = head
    #     curr = head.next
    #     while curr and curr.data <= L.data:
    #         last = curr
    #         curr = curr.next
    #     L.next = last.next
    #     last.next = L
    #     L = L_next

    # return head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sort_list.py", "sort_list.tsv", stable_sort_list
        )
    )
