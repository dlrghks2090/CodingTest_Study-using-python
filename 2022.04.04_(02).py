# 백준_실버3_2193번_이친수 문제
N = int(input())

dp = [[0]*2 for  i in range(91)]

dp[1][0] = 0 # 해당 위치의 자리에 0이 올때
dp[1][1] = 1 # 해당 위치의 자리에 1이 올때
#dp[2][0] = 1
#dp[2][1] = 0
#dp[3][0] = dp[2][0] + dp[2][1]
#dp[3][1] = dp[2][0]

if N == 1:
    print(1)
    exit()

for i in range(2, N+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    # 새로운 자리의 수가 1이오려면 이전 수가 0이어야 하므로
    dp[i][1] = dp[i - 1][0]

print(dp[N][0] + dp[N][1])