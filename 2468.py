import sys
from collections import deque



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]


x = [-1,1,0,0]
y = [0,0,-1,1]






def BFS(x,y,graph,visit):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        
        
        
        
        