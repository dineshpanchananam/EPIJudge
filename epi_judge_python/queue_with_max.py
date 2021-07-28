from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax:
  def __init__(self):
    self.q = deque()
    self.mq = deque()

  def enqueue(self, x: int) -> None:
    self.q.append(x)
    max_q = self.mq
    while max_q and max_q[-1] < x:
      max_q.pop()
    max_q.append(x)

  def dequeue(self) -> int:
    popped = self.q.popleft()
    if popped == self.mq[0]:
      self.mq.popleft()
    return popped

  def max(self) -> int:
    return self.mq[0]

def queue_tester(ops):

  try:
    q = QueueWithMax()

    for (op, arg) in ops:
      if op == 'QueueWithMax':
        q = QueueWithMax()
      elif op == 'enqueue':
        q.enqueue(arg)
      elif op == 'dequeue':
        result = q.dequeue()
        if result != arg:
          raise TestFailure('Dequeue: expected '+str(arg)+', got '+str(result))
      elif op == 'max':
        result = q.max()
        if result != arg:
          raise TestFailure('Max: expected '+str(arg)+', got '+str(result))
      else:
        raise RuntimeError('Unsupported queue operation: '+op)
  except IndexError:
    raise TestFailure('Unexpected IndexError exception')

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('queue_with_max.py', 'queue_with_max.tsv',
                                   queue_tester))
