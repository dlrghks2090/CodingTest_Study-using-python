#백준_실버1_10844번_쉬운 계단 수 문제

# 101행 10열의 행렬을 만든다.
# 열은 0 ~ 9 인덱스까지 사용
# 행은 1 ~ 100 까지 사용 (최대)
dp = [[0]*10 for i in range(101)]

N = int(input())

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for m in range(10):
        # 0번째는 이전단계의 1번째 에서만 올 수 있으므로
        if m == 0:
            dp[i][m] = dp[i-1][1]
        # 9번째는 이전단계의 8번째 에서만 올 수 있으므로
        elif m == 9:
            dp[i][m] = dp[i-1][8]
        # 이 외의 자리는 이전단계의 양 옆 자리에서 올 수 있으므로
        else:
            dp[i][m] = dp[i-1][m-1] + dp[i-1][m+1]


sol = 0

# 최종 결과가짓수를 모두 더해준다.
for idx in range(10):
    sol = sol + dp[N][idx]

print(sol % 1000000000)