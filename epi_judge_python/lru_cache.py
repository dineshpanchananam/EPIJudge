from test_framework import generic_test
from test_framework.test_failure import TestFailure

# class Node:
#   def __init__(self, k, v, p=None, n=None):
#     self.key = k
#     self.value = v
#     self.prev = p
#     self.next = n

# def unlink(n: Node):
#   n.prev.next = n.next
#   n.next.prev = n.prev
#   # n.prev = n.next = None
#   return n

# def prepend(n: Node, head: Node):
#   n.next = head.next
#   n.prev = head
#   head.next.prev = n
#   head.next = n

# class LruCache:
#   def __init__(self, capacity: int) -> None:
#     self.cap = capacity
#     self.map = {}
#     self.head = self.tail = Node("+", "-")
#     # self.tail = Node("-", "+")
#     self.head.next = self.tail
#     self.tail.prev = self.head

#   def lookup(self, isbn: int) -> int:
#     if isbn not in self.map:
#       return -1

#     node = unlink(self.map[isbn])
#     prepend(node, self.head)
#     return node.value

#   def insert(self, isbn: int, price: int) -> None:
#     if isbn in self.map:
#       self.lookup(isbn)
#       return

#     if len(self.map) >= self.cap:
#       last = self.tail.prev
#       unlink(last)
#       del self.map[last.key]

#     new_node = Node(isbn, price)
#     self.map[isbn] = new_node
#     prepend(new_node, self.head)

#   def erase(self, isbn: int) -> bool:
#     if isbn not in self.map:
#       return False

#     node = self.map[isbn]
#     unlink(node)
#     del self.map[isbn]
#     return True

from collections import OrderedDict

class LruCache:
  def __init__(self, capacity: int) -> None:
    self.cap = capacity
    self.map = OrderedDict()

  def lookup(self, isbn: int) -> int:
    if isbn not in self.map:
      return -1
    self.map.move_to_end(isbn)
    return self.map[isbn]

  def insert(self, isbn: int, price: int) -> None:
    if isbn in self.map:
      self.lookup(isbn)
      return

    if len(self.map) >= self.cap:
      self.map.popitem(last=False)

    self.map[isbn] = price

  def erase(self, isbn: int) -> bool:
    return bool(self.map.pop(isbn, None))

def lru_cache_tester(commands):
  if len(commands) < 1 or commands[0][0] != "LruCache":
    raise RuntimeError("Expected LruCache as first command")

  cache = LruCache(commands[0][1])

  for cmd in commands[1:]:
    if cmd[0] == "lookup":
      result = cache.lookup(cmd[1])
      if result != cmd[2]:
        raise TestFailure("Lookup: expected "+str(cmd[2])+", got "+str(result))
    elif cmd[0] == "insert":
      cache.insert(cmd[1], cmd[2])
    elif cmd[0] == "erase":
      result = 1 if cache.erase(cmd[1]) else 0
      if result != cmd[2]:
        raise TestFailure("Erase: expected "+str(cmd[2])+", got "+str(result))
    else:
      raise RuntimeError("Unexpected command "+cmd[0])

if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("lru_cache.py", "lru_cache.tsv",
                                   lru_cache_tester))
