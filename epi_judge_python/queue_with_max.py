from test_framework import generic_test
from test_framework.test_failure import TestFailure
from stack_with_max import Stack


class QueueWithMax:
  def __init__(self):
    self.enq = Stack()
    self.deq = Stack()

  def enqueue(self, x: int) -> None:
    self.enq.push(x)

  def dequeue(self) -> int:
    if self.deq.empty():
      while not self.enq.empty:
        self.deq.push(self.end.pop())
    return self.deq.pop()

  def max(self) -> int:
    if self.deq.empty():
      while not self.enq.empty:
        self.deq.push(self.enq.pop())
    return self.deq.max()


def queue_tester(ops):

  try:
    q = QueueWithMax()

    for (op, arg) in ops:
      if op == "QueueWithMax":
        q = QueueWithMax()
      elif op == "enqueue":
        q.enqueue(arg)
      elif op == "dequeue":
        result = q.dequeue()
        if result != arg:
          raise TestFailure("Dequeue: expected "+str(arg)+", got "+str(result))
      elif op == "max":
        result = q.max()
        if result != arg:
          raise TestFailure("Max: expected "+str(arg)+", got "+str(result))
      else:
        raise RuntimeError("Unsupported queue operation: "+op)
  except IndexError:
    raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
  exit(
    generic_test.generic_test_main("queue_with_max.py", "queue_with_max.tsv",
                                   queue_tester))
