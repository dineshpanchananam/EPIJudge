from test_framework import generic_test

def power(x: float, y: int) -> float:
  if x == 0:
    return 0
  elif y < 0:
    return power(1/x, abs(y))
  elif y == 0:
    return 1
  elif y == 1:
    return x
  half = power(x, y >> 1)
  return half*half*(x if y & 1 else 1)

if __name__ == "__main__":
  exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
