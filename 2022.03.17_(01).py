# 테스트 케이스 수 입력
T = int(input())

i = 0
while i < T:
    # 문장 입력
    arr = input()
    ox = 0 # 왼쪽 괄호가 더 많은 경우 중복된 출력을 하지 않기 위해 사용
    st = [] # 스택
    for a in arr:
        if a == '(':
            st.append(i)
        elif a == ')':
            if not st:
                print("NO")
                ox = 1 #스택이 비어있을때, 오른쪽괄호가 나오면 'NO'를 출력하고 ox를 체크
                break
            else:
                st.pop()
    # 스택이 비어있을때, 오른쪽 괄호가 나온 경우를 제외한 나머지 경우들의 결과 출력
    if ox == 0:
        # 스택에 아무것도 남지 않았다면 VPS이므로 'YES'출력
        if not st:
            print("YES")
        # 스택에 '('가 남아있으면 왼쪽괄호가 더 많은것이므로 'NO'출력
        else:
            print("NO")
    # 테스트케이스 수만큼 루프를 동작시키기 위한 변수 설정
    i = i + 1