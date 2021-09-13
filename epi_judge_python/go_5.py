def msh(i, a, c):
  if i == len(a):
    return 0
  if not c:
    return 0
  res = 0
  for k in range(i, len(a)):
    if c >= a[k]:
      res = max(res, a[k]+msh(k+1, a, c-a[k]))
  return res

def ms(a, c):
  print(msh(0, a, c))

ads = [1, 3, 4]
cap = 11
dp = [0]*(cap+1)
dp[0] = 1
for ad in ads:
  for c in range(cap+1):
    if dp[c] == 1 and c+ad <= cap:
      dp[c+ad] = 2
  for c in range(cap+1):
    if dp[c] == 2:
      dp[c] = 1

print(dp)
for c in range(cap, -1, -1):
  if dp[c] == 1:
    print(f"max spend: {c}")
    break

ms(ads, cap)