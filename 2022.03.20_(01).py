# 백준_큐_실버4_10845번_큐 문제
import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])