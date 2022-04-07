# 백준_실버2_1912번_연속합 문제
n = int(input())

arr = list(map(int, input().split()))

dp = [0 for i in range(n)]
sol = arr[0]

dp[0] = arr[0]

for i in range(1, n):
    if dp[i-1] + arr[i] > arr[i]:
        dp[i] = dp[i-1] + arr[i]
        sol = max(sol, dp[i])
    else:
        dp[i] = arr[i]
        sol = max(sol, dp[i])
print(sol)