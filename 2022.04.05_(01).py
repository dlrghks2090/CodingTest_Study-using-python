# 백준_실버2_11053번_가장 긴 증가하는 부분 수열 문제
N = int(input())

# sol은 현재 위치까지의 최대 부분수열 개수를 나타내는 배열이다.
# 자기 자신을 포함하면 최소 1개이기 때문에 1로 초기화해준다.
sol = [1]*1002

arr = [0] + list(map(int, input().split()))
max_sol = 1

for i in range(2, N+1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            if sol[i] < sol[j] + 1:
                sol[i] = sol[j] + 1

    max_sol = max(sol[i], max_sol)

#print(sol)
#print(arr)
print(max_sol, end ='')