import sys
from collections import deque

T = int(input())
L = [-1,1,0,0]
H = [0,0,-1,1]




for i in range(T):
    M,N,K = map(int,input().split())
    for j in range(K):
        X,Y = map(int,input().split())
        
        
visit = [[False] * N for _ in range(M)]
graph = [[] for _ in range()]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    
    while queue:
        queue.popleft()
        

        
        
