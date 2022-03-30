# 백준_실버4_11656번_접미사 배열 문제
str = input()

arr = []

for i in range(len(str)):
    arr.append(str[i:len(str)])

arr.sort()

for i in range(len(arr)):
    print(arr[i])