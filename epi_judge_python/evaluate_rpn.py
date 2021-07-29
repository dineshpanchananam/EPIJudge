from test_framework import generic_test

from operator import add, sub, mul, floordiv as div

def evaluate(expression: str) -> int:
  st = expression.split(",")[::-1]
  values = []
  cmds = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
  }
  while st:
    cmd = st.pop()
    if cmd in "-+/*":
      a, b = values.pop(), values.pop()
      values.append(cmds[cmd](b, a))
    else:
      values.append(int(cmd))
  return values[0]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                   evaluate))
