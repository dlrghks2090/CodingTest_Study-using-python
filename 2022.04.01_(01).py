#백준_실버4_1978번_소수 찾기 문제
N = input()

N = int(N)

arr = input().split()

for i in range(N):
    arr[i] = int(arr[i])


sol = 0
for i in range(N):
    j = 1
    flag = 0
    while arr[i] >= j:
        if arr[i] % j == 0:
            flag = flag + 1
        j = j + 1
    if flag == 2:
        sol = sol + 1

print(sol)