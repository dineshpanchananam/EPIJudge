def reverse_bits(x) -> int:
  print(bin(x))
  y = 1
  while x:
    y = (y << 1)+(x & 1)
    x >>= 1
  print(bin(y))
  # return y

# print(reverse_bits(int('0b100001011', 2)))
# print(reverse_bits(1351510410656))
def conv(x):
  y = str(bin(x))[2:]
  y = '0'*(64-len(y))+y
  return f"0b{y}"

print(conv(1351510410656))
print(conv(405942121183313920))