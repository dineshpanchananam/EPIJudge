from list_node import ListNode
from test_framework import generic_test
from utils.list_node import rev, mid

<<<<<<< HEAD:epi_judge_python/is_list_palindromic.py
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    return True

=======
def is_linked_list_a_palindrome(L):
  m = mid(L)
  m = rev(m)
  while m and L:
    if L.data != m.data:
      return False
    m, L = m.next, L.next
  return True
>>>>>>> 7fdc011... 01.04:epi_judge_python/done/is_list_palindromic.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
