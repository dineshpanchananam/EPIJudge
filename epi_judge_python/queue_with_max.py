from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque
import heapq as h

class QueueWithMax:
<<<<<<< HEAD
    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        return

    def dequeue(self) -> int:
        # TODO - you fill in here.
        return 0
=======
    def __init__(self):
      self.q = deque()
      self.maxq = deque()

    def enqueue(self, x):
      self.q.append(x)
      if q.

    def dequeue(self):
      if 
>>>>>>> 6e7e48e... some wip

    def max(self) -> int:
        # TODO - you fill in here.
        return 0


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
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
