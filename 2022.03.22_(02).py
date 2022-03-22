# 백준_실버3_17413번_단어 뒤집기2 문제
str = input()
arr = []
flag = 0
a = 0
b = 0
count = 0
for i in range(len(str)):
    if str.find('<') < 0:
        arr = []
        arr = str.split()
        for j in range(len(arr)):
            str2 = []
            str2 = ''.join(reversed(arr[j]))
            print(str2, end = ' ')
        break
    else:
        if str[i] == '<':
            if count > 0:
                b = i-1
                tmp = str[a:b+1].split()
                for j in range(len(tmp)):
                    str2 = []
                    str2 = ''.join(reversed(tmp[j]))
                    if j == len(tmp)-1:
                        print(str2, end='')
                    else:
                        print(str2, end=' ')
                count = 0
            flag = 1
            a = i

        elif str[i] == '>':
            flag = 0
            b = i
            print(str[a:b+1], end='')
            a = 0
            b = 0
        elif flag == 0:
            if count == 0:
                a = i
            count = count + 1
if count > 0:
    b = len(str)-1
    tmp = str[a:b + 1].split()
    for j in range(len(tmp)):
        str2 = []
        str2 = ''.join(reversed(tmp[j]))
        if j == len(tmp) - 1:
            print(str2, end='')
        else:
            print(str2, end=' ')



