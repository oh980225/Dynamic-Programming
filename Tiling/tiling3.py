# 3. 타일채우기 타일링3(백준 2133번)
# 문제에서 찾은 점화식: D[n] = 3*D[n-2] + (2*D[n-4] + 2*D[n-6] + 2*D[n-8] + ... + 2*D[0])
memo = [0 for i in range(1001)]
def dp(x):
  if x == 0:
    return 1
  if x == 1:
    return 0
  if x == 2:
    return 3
  if memo[x] != 0:
    return memo[x]
  result = 3*dp(x-2)
  for i in range(3, x+1):
    if x%2 == 0:
      result += 2*dp(x-i)
  memo[x] = result
  return memo[x]

x = int(input())
print(dp(x))