import sys

# 시간복잡도를 줄이기 위해 sys.stdin.readline() 을 사용해주었고
# 개행의 입력을 제외하기 위해서 위의 입력 명령어 뒤에 stirp()을 붙여주었다.
N = int(sys.stdin.readline().strip())
i = 0
st =[]

while i < N:
    work = sys.stdin.readline().strip()
    num = 0
    if 'push' in work:
        a, b = work.split()
        num = int(b)
        st.append(num)
    elif work == 'pop':
        if not st:
            print(-1)
        else:
            print(st[-1])
            st.pop()
    elif work == 'size':
        print(len(st))
    elif work == 'empty':
        if not st:
            print(1)
        else:
            print(0)
    elif work == 'top':
        if not st:
            print(-1)
        else:
            print(st[-1])
    i = i + 1
