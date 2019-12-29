from list_node import ListNode
from test_framework import generic_test

<<<<<<< HEAD:epi_judge_python/search_in_list.py

def search_list(L: ListNode, key: int) -> ListNode:
    # TODO - you fill in here.
    return ListNode()

=======
def search_list(L, key):
  curr = L
  while curr and curr.data != key:
    curr = curr.next
  return curr
>>>>>>> cf3ad5a... solved some:epi_judge_python/done/search_in_list.py

def search_list_wrapper(L, key):
    result = search_list(L, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_list.py',
                                       'search_in_list.tsv',
                                       search_list_wrapper))
