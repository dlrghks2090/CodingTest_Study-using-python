# 백준_실버5_1158번_요세푸스 문제_파이썬 풀이
import sys
N, K= sys.stdin.readline().split()

N = int(N)
K = int(K)

list = []
sol = []
for i in range(N):
    list.append(i + 1)

num = -1
while list:
    for j in range(K):
        num = num + 1
        if num > (len(list) - 1):
            num = num - (len(list) - 1) - 1
    sol.append(list.pop(num))
    num = num - 1

print('<', end='')
for a in range(len(sol)-1):
    print(sol[a], end=', ')
print(sol[len(sol)-1], end='>')