def reverse_bits(x) -> int:
  print(bin(x))
  y = 0
  while x:
    y = (y << 1)+(x & 1)
    x >>= 1
  print(bin(y))
  # return y

print(reverse_bits(int('0b100001011', 2)))