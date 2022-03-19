# 백준_스택_실버3_1406번_에디터 문제

# sys를 import 하여 sys.stdin.readline() 으로 러닝타임을 줄입니다.
# 두개의 list를 스택처럼 사용하여 시간복잡도를 줄여주었습니다.
import sys
st_list = list(sys.stdin.readline().rstrip())
tmp_list = []
point = len(st_list) - 1
M = int(sys.stdin.readline())

for _ in range(M):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st_list:
            tmp_list.append(st_list[-1])
            st_list.pop()
    elif command[0] == 'D':
        if tmp_list:
            st_list.append(tmp_list[-1])
            tmp_list.pop()
    elif command[0] == 'B':
        if st_list:
            st_list.pop()
    elif command[0] == 'P':
        st_list.append(command[1])
while tmp_list:
    st_list.append(tmp_list.pop())

print("".join(st_list))