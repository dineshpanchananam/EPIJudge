from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Queue:
  def __init__(self, capacity: int) -> None:
    # TODO - you fill in here.
    self.n = 0
    self.cap = capacity
    self.data = [0]*capacity
    self.head, self.tail = 0, 0

  def enqueue(self, x: int) -> None:
    self.data[self.tail] = x
    self.n += 1
    self.tail += 1
    self.tail %= self.cap

  def dequeue(self) -> int:
    value = self.data[self.head]
    self.head += 1
    self.head %= self.cap
    self.n -= 1
    return value

  def size(self) -> int:
    return self.n

def queue_tester(ops):
  q = Queue(1)

  for (op, arg) in ops:
    if op == 'Queue':
      q = Queue(arg)
    elif op == 'enqueue':
      q.enqueue(arg)
    elif op == 'dequeue':
      result = q.dequeue()
      if result != arg:
        raise TestFailure('Dequeue: expected '+str(arg)+', got '+str(result))
    elif op == 'size':
      result = q.size()
      if result != arg:
        raise TestFailure('Size: expected '+str(arg)+', got '+str(result))
    else:
      raise RuntimeError('Unsupported queue operation: '+op)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('circular_queue.py', 'circular_queue.tsv',
                                   queue_tester))
