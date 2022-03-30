# 백준_브론즈5_10430번_나머지 문제

arr = []
arr = input().split()

A = int(arr[0])
B = int(arr[1])
C = int(arr[2])

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)