# 다이나믹 프로그래밍의 가정
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함한 큰 문제에도 동일하다.

# memoization 활용!
memo = [0 for i in range(100)]

def fivo(x):
  if x == 1:
    return 1
  if x == 2:
    return 1
  if memo[x] != 0:
    return memo[x]
  memo[x] = fivo(x-1) + fivo(x-2)
  return memo[x]

print(fivo(30))