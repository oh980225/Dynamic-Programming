# 4. 타일채우기3 타일링4(백준 14852번)
# 문제에서 찾은 점화식: D[n] = 2*D[n-1] + 3*D[n-2] + (2*D[n-3] + 2*D[n-4] + 2*D[n-5] + ... + 2*D[0])
memo = [[0, 0] for i in range(1000001)]

def dp(x):
  memo[0][0] = 1
  memo[1][0] = 2
  memo[2][0] = 7
  for i in range(3, x+1):
    memo[i][1] = (memo[i-1][1] + memo[i-3][0]) % 1000000007
    memo[i][0] = (3*memo[i-2][0] + 2*memo[i-1][0] + 2*memo[i][1]) % 1000000007
  return memo[x][0]

x = int(input())
print(dp(x))