from test_framework import generic_test

def rev(x):
  tail = x
  curr, p = x, None
  while curr:
    curr, tmp = p, curr.next
    p, curr = curr, tmp
  return p, tail

def detach(L, idx):
  curr, prev = L, None
  for _ in range(idx):
    if curr:
      prev = curr
      curr = curr.next
  if prev:
    nxt = prev.next
    prev.next = None
    return prev, nxt


def reverse_sublist1(L, start, finish):
  if L and L.next and (finish - start) > 1:
    _, head3 = detach(L, finish)
    end1, head2 = detach(L, start)
    head2, tail = rev(head2)
    tail.next = head3
    end1.next = head2
  return L

def reverse_sublist1(L, start, finish):
  ptr1, prev = L, None
  for _ in range(start-1):
    prev = head
    head = head.next
  left = None
  curr = head
  for _ in range(start, finish):
    if head:
      tmp = head.next
      head.next = left
      left, head = head, tmp
  if head:

  if left:
    if prev:
      prev.next = left
      L = 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
