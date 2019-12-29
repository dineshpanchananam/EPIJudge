from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
<<<<<<< HEAD:epi_judge_python/stack_with_max.py
    def empty(self) -> bool:
        # TODO - you fill in here.
        return True

    def max(self) -> int:
        # TODO - you fill in here.
        return 0

    def pop(self) -> int:
        # TODO - you fill in here.
        return 0

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        return
=======
    def __init__(self):
      self.maxs = []
      self.data = []

    def empty(self):
      return not bool(self.data)

    def max(self):
      if self.maxs:
        return self.maxs[-1]

    def pop(self):
      if self.data:
        popped = self.data.pop()
        if popped == self.max():
          self.maxs.pop()
        return popped

    def push(self, x):
      if (not self.maxs) or (x >= self.max()):
        self.maxs.append(x)
      self.data.append(x)
>>>>>>> cf3ad5a... solved some:epi_judge_python/done/stack_with_max.py


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
