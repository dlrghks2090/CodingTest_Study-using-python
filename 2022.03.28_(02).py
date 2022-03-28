# 백준_브론즈2_10808번_알파벳 개수 문제
str = list(input())

sol = [0]*26

for i in range(len(str)):
    for j in range(26):
        if ord(str[i]) == ord('a') + j:
            sol[j] = sol[j] + 1
            break

for i in range(26):
    print(sol[i], end=' ')