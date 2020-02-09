# 2. 2xn 타일링2(백준 11727번)
# 문제에서 찾은 점화식: D[n] = D[n-1] + 2*D[n-2]

memo = [0 for i in range(1001)]

def dp(x):
  if x == 1:
    return 1
  if x == 2:
    return 3
  if memo[x] != 0:
    return memo[x]
  memo[x] = (dp(x-1) + 2*dp(x-2)) % 10007
  return memo[x]

x = int(input())
print(dp(x))