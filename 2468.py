import sys
from collections import deque



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]



dx = [-1,1,0,0]
dy = [0,0,-1,1]






def BFS(x,y,h,v):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0 <= ny < N:
                if not visit[nx][ny] and graph[nx][ny] > h :
                    visit[nx][ny] = True
                    queue.append((nx,ny))
                    

                    
            
max_height = max(max(row) for row in graph)
answer = 1

for h in range(max_height+1):
    visit = [[False] * N for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and graph[i][j] > h :
                BFS(i,j,h,visit)
                count += 1
    answer = max(answer,count)
    
print(answer)
            
    
    
    
        