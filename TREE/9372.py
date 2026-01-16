import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input()  # 비행기 정보는 읽기만 하고 버림
    print(N - 1)
