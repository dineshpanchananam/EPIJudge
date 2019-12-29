def p(x):
  s = []
  while x:
    s.append(x.data)
    x = x.next
  print(s)

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

x = N(1, N(2, N(3, N(4, N(8)))))
p(x)
m = mid(x)
p(m)
p(x)