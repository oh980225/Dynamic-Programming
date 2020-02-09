# 1. 2xn 타일링(백준 11726번)
# 문제에서 찾은 점화식: D[n] = D[n-1] + D[n-2]

memo = [0 for i in range(1001)]

def dp(x):
  if x == 1:
    return 1
  if x == 2:
    return 2
  if memo[x] != 0:
    return memo[x]
  memo[x] = (dp(x-1) + dp(x-2)) % 10007
  return memo[x]

x = int(input())
print(dp(x))