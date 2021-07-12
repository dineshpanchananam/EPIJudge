from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Node:
  def __init__(self, v, p=None, n=None):
    self.data = v
    self.prev = p
    self.next = n

def delete(n: Node):
  prev = n.prev
  next = n.next
  prev.next = next
  next.prev = prev

def move_to_front(n: Node, h: Node):
  n.next = h
  h.prev = n
  return n

class LruCache:
  def __init__(self, capacity: int) -> None:
    self.cap = capacity
    self.map = {}
    self.head = self.tail = Node("-")

  def lookup(self, isbn: int) -> int:
    if isbn in self.map:
      return self.map[isbn].data
    return -1

  def insert(self, isbn: int, price: int) -> None:
    self.erase(isbn)
    if len(self.map) >= self.cap:
      self.tail = self.tail.prev
      self.tail.next = None

    new_node = Node(price, self.head, self.head.next)
    self.head.next = new_node
    self.map[isbn] = new_node
    self.cap += 1

  def erase(self, isbn: int) -> bool:
    if isbn in self.map:
      delete(self.map[isbn])
      del self.map[isbn].data
      return True
    return False

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
