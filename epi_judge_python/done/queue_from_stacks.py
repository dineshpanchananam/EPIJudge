from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
<<<<<<< HEAD:epi_judge_python/queue_from_stacks.py
    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        return

    def dequeue(self) -> int:
        # TODO - you fill in here.
        return 0

=======
    def __init__(self):
      self.s = []
      self.ptr = 0
    
    def enqueue(self, x):
      self.s.append(x)

    def dequeue(self):
      if self.s:
        self.ptr += 1
        return self.s[self.ptr-1]
>>>>>>> 6e7e48e... some wip:epi_judge_python/done/queue_from_stacks.py

def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
