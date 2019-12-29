from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def mid(x):
	c, f, prev = x, x, x
	while f and f.next:
		prev = c
		c = c.next
		f = f.next.next
	tmp = prev.next
	prev.next = None
	return tmp

<<<<<<< HEAD
def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None
=======
def zipping_linked_list(L):
  return mid(L)
>>>>>>> cf3ad5a... solved some


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
