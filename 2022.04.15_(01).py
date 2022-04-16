# 백준_브루트포스_1476번_실버5_날짜 계산 문제
E, S, M = map(int, input().split())

count = 0
arr = [0 for i in range(3)]
while 1:
    arr[0] += 1
    arr[1] += 1
    arr[2] += 1
    count += 1
    if arr[0] > 15:
        arr[0] = 1
    if arr[1] > 28:
        arr[1] = 1
    if arr[2] > 19:
        arr[2] = 1

    if arr[0] == E and arr[1] == S and arr[2] == M:
        break

print(count)