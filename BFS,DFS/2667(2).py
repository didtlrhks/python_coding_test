import sys
from collections import deque

N = int(input())
visit = [[False] * N for _ in range(N)]
graph = [list(input().sprit()) for _ in range(N)]

result = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    visit[x][y] = True
    count = 1
    
    while queue:
        x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N: 
        if not visit[nx][ny] and graph[nx][ny] == '1':
            visit[nx][ny] == True
            queue.append((nx,ny))
            count += 1
            
    return count

    
for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] == '1':
            result.append((BFS(i,j)))
            
result.sort()



print(len(result))   
for r in result:
    print(r)
            
            
    