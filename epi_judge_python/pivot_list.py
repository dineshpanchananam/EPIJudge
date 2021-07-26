import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
  le = lp = ListNode()
  eq = ep = ListNode()
  gt = gp = ListNode()
  while l:
    if l.data == x:
      ep.next = l
      ep = ep.next
    elif l.data > x:
      gp.next = l
      gp = gp.next
    else:
      lp.next = l
      lp = lp.next
    l = l.next

  gp.next = None
  ep.next = gt.next
  lp.next = eq.next
  return le.next

  # lp = ep = gp = None
  # while l:
  #   next = l.next
  #   if l.data < x:
  #     l.next = lp
  #     lp = l
  #   elif l.data == x:
  #     l.next = ep
  #     ep = l
  #   else:
  #     l.next = gp
  #     gp = l
  #   l = next

  # pp = None
  # for part in [gp, ep, lp]:
  #   while part:
  #     next = part.next
  #     part.next = pp
  #     pp = part
  #     part = next
  # return pp

def linked_to_list(l):
  v = list()
  while l is not None:
    v.append(l.data)
    l = l.next
  return v

@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
  original = linked_to_list(l)

  l = executor.run(functools.partial(list_pivoting, l, x))

  pivoted = linked_to_list(l)
  mode = -1
  for i in pivoted:
    if mode == -1:
      if i == x:
        mode = 0
      elif i > x:
        mode = 1
    elif mode == 0:
      if i < x:
        raise TestFailure('List is not pivoted')
      elif i > x:
        mode = 1
    else:
      if i <= x:
        raise TestFailure('List is not pivoted')

  if sorted(original) != sorted(pivoted):
    raise TestFailure('Result list contains different values')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                   list_pivoting_wrapper))
