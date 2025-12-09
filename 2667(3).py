import sys
from collections import deque

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []


def BFS(x,y):
    queue = deque()
    count = 1
    visit[x][y] = True
    

while queue:
    x,y = queue.popleft()
    queue.append((x,y))
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
    if 0 <= nx < N and 0 <= ny < N:
        
    
    
    
    
    
    
    
    