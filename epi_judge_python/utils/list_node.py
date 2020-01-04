def p(x):
  s = []
  while x:
    s.append(x.data)
    x = x.next
  print(s)

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

class N:
  def __init__(self, d, l=None):
    self.data = d
    self.next = l

fst = N(1, N(2, N(3, N(4, N(5)))))
snd = rev(mid(fst))

head = fst
while snd:
  tmp = snd.next
  snd.next = fst.next
  fst.next = snd
  snd, fst = tmp, snd.next
p(head)