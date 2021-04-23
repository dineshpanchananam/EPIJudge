from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fst = L
    while fst:
        slow = slow.next
        fst = fst.next
        if fst:
            fst = fst.next
    tmp = None
    while slow:
        next = slow.next
        slow.next = tmp
        tmp, slow = slow, next
    while tmp and tmp.data == L.data:
        L, tmp = L.next, tmp.next
    return not tmp


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
