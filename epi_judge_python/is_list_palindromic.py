from list_node import ListNode
from test_framework import generic_test

def recur(a, b):
  if not b:
    return a, True
  c, sub = recur(a, b.next)
  return c.next, sub and (c.data == b.data)

def is_linked_list_a_palindrome_rec(L: ListNode) -> bool:
  return recur(L, L)[1]

def reverse(r):
  new = None
  while r:
    r_next = r.next
    r.next = new
    new, r = r, r_next
  return new

def is_linked_list_a_palindrome(L: ListNode) -> bool:
  if L and L.next:
    s = f = L
    prev = None
    while f and f.next:
      f = f.next.next
      if f: s = s.next

    s1 = reverse(s.next)
    s.next = None
    f, s = L, s1
    while s and s.data == f.data:
      s = s.next
      f = f.next
    return not s

  return True

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_list_palindromic.py',
                                   'is_list_palindromic.tsv',
                                   is_linked_list_a_palindrome))
