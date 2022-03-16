import sys

T = int(input())

i = 0

while i < T:
    str1 = input()
    list = str1.split(' ')
    for arr in list:
        j = 1
        while j <= len(arr):
            print(arr[len(arr)-j], end = '')
            j = j + 1
        print(end = ' ')
    print()
    i = i + 1