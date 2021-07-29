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
      a, b = values.pop(), values.pop()
      values.append(ops[token](b, a))
    else:
      values.append(int(token))
  return values[0]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                   evaluate))
