import sys
from collections import deque

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]



print(graph)

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    count = 1 
    
    while queue:
        x,y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            

    
    
    
    