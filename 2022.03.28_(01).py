# 백준_실버3_1935번_후위표기식2 문제
N = int(input())

str1 = input()
str = list(str1)  # list()를 사용해서 문자열을 문자로 나눠 리스트화했다.

num = []
for i in range(N):
    a = int(input())
    num.append(a)

for j in range(len(str)):
    for k in range(26):
        # ord()를 사용하여 char형식을 아스키코드화하여 문자를 비교했다.
        if ord(str[j]) == ord('A') + k:
            # 같은 문자를 찾게 되면 해당 문자자리에 맞는 수로 재할당 해주었다.
            str[j] = num[k]
            break

sol = []    #스택방식으로 후위표기식을 계산하기위한 빈 리스트 설정
for i in range(len(str)):
    # 스택의 가장 위에있는 두 개의 수를 계산하고 두 수를 삭제시킨다. 후에 계산한 수를 다시 푸쉬한다.
    if str[i] == '+':
        tmp = sol[-2] + sol[-1]
        sol.pop()
        sol.pop()
        sol.append(tmp)
    elif str[i] == '-':
        tmp = sol[-2] - sol[-1]
        sol.pop()
        sol.pop()
        sol.append(tmp)
    elif str[i] == '*':
        tmp = sol[-2] * sol[-1]
        sol.pop()
        sol.pop()
        sol.append(tmp)
    elif str[i] == '/':
        tmp = sol[-2] / sol[-1]
        sol.pop()
        sol.pop()
        sol.append(tmp)
    else:
        sol.append(str[i])
# 최종적으로 나온 결과값을 소수점 2번째자리까지 출력하기위해 f'{출력값:.2f}' 를 사용해 print해주었다.
print(f'{sol[0]:.2f}')