from test_framework import generic_test

def rev(x):
  p, c = None, x
  while c:
    nxt, c.next = c.next, p
    p, c = c, nxt
  return p

def mid(x):
  c, f = x, x
  while f and f.next:
    c = c.next
    f = f.next.next
  if c:
    tmp = c.next
    c.next = None
    return tmp

def zipping_linked_list(fst):
	snd = rev(mid(fst))
	head = fst
	while snd:
		tmp = snd.next
		snd.next = fst.next
		fst.next = snd
		snd, fst = tmp, snd.next
	return head

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
