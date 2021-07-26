import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
  if l0 and l1:
    p1, p2 = l0, l1
    while p1 and p2 and p1 != p2:
      p1, p2 = p1.next, p2.next
      if not p1:
        p1 = l1
      elif not p2:
        p2 = l0
    return p2

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
  if common:
    if l0:
      i = l0
      while i.next:
        i = i.next
      i.next = common
    else:
      l0 = common

    if l1:
      i = l1
      while i.next:
        i = i.next
      i.next = common
    else:
      l1 = common

  result = executor.run(functools.partial(overlapping_no_cycle_lists, l0, l1))

  if result != common:
    raise TestFailure('Invalid result')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                   'do_terminated_lists_overlap.tsv',
                                   overlapping_no_cycle_lists_wrapper))
