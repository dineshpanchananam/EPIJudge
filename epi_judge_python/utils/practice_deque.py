from collections import deque
from collections import 
d = deque()
d.append(10)
d.append(20)
d.appendleft(30)
d.appendleft(40)
while d:
  print(d.popleft())

a = []
push = a.append
push(1)
push(2)
push(3)
# print(a.index(2))
itr = iter(a)
for i in itr:
  print(i)

b = [4, 3, 2, 1]
a = []
n = len(b)
for i in range(n):
  a.append(b.pop())
b = a
print(b)
# while a:
#   print(a.pop())
