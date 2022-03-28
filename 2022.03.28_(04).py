# 백준_브론즈1_11655번_ROT13문제

str = list(input())

for i in range(len(str)):

    if str[i] == ' ':
        continue
    elif ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
        if ord(str[i]) + 13 > ord('z'):
            str[i] = chr(ord(str[i]) + 13 - 26)
        else:
            str[i] = chr(ord(str[i]) + 13)
    elif ord(str[i]) >= ord('A') and ord(str[i]) <= ord('Z'):
        if ord(str[i]) + 13 > ord('Z'):
            str[i] = chr(ord(str[i]) + 13 - 26)
        else:
            str[i] = chr(ord(str[i]) + 13)
    elif int(str[i]) >= 0 and int(str[i]) <= 9:
        continue

for i in range(len(str)):
    print(str[i], end='')