from test_framework import generic_test

from operator import add, sub, mul, floordiv as div

def evaluate(expression: str) -> int:
  ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
  }
  values = []
  for token in expression.split(","):
    if token in ops:
      values.append(ops[token](values.pop(), values().pop()))
    else:
      values.append(int(token))
  return values[-1]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                   evaluate))
