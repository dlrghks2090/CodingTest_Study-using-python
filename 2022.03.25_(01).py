# 백준_실버3_10799번_쇠막대기 문제
import sys

str = sys.stdin.readline().rstrip()

count = 0;
st = []
sol = 0

for i in range(len(str)):
    if str[i] == '(':
        count = count + 1
    elif str[i] == ')':
        count = count - 1
        if str[i - 1] == '(':
            if count != 0:
                sol = sol + count
        else:
            sol = sol + 1


sol = sol + count

print(sol)
