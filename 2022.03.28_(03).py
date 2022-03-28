# 백준_브론즈2_10820번_문자열 분석 문제
while (1):
    try:
        str = list(input())

    except:break

    sol = [0]*4

    for i in range(len(str)):

        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('a') + 25:
            sol[0] = sol[0] + 1
        elif ord(str[i]) >= ord('A') and ord(str[i]) <= ord('A') + 25:
            sol[1] = sol[1] + 1
        elif str[i] == ' ':
            sol[3] = sol[3] + 1
        elif int(str[i]) >= 0 and int(str[i]) <= 9:
            sol[2] = sol[2] + 1

    for idx in range(3):
        print(sol[idx], end = ' ')
    print(sol[3])
