# 백준_실버5_2609번_최대공약수와 최소공배수 문제

arr = input().split()
a = int(arr[0])
b = int(arr[1])

num = 1
min = 0
sol = 1

if a < b :
    min = a
else:
    min = b


while num <= min:

	if a % num == 0 and b % num == 0:
		sol = num
	num += 1


print(sol)
print(round(a * b / sol), end='')