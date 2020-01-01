from test_framework import generic_test


def power(x, y):
  sign = bool(y < 0)
  y = abs(y)
  if y == 0:
    return 1
  elif y == 1:
    return 1.0 / x if sign else x
  m = y >> 1
  p = power(x, m)
  p *= p
  odd = p * (x if y & 1 else 1)
  return (1.0 / odd) if sign else odd

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
