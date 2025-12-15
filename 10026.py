import sys
from collections import deque


N = int(input())
graph = list([] for _ in range(N))# 문법을 모르겠음 아마 문자열을 받는거면 될거같은데.. 
visit = [False] * N
count = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(N):
    for j in range(N):
        graph[i][j] = # 여기에다가 문자열을 넣어야 되고 
    
    

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    

    
    while queue:
        x,y = queue.popleft()      
        queue.append((x,y))
        
        
        for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        
        if 0 <= nx < N and 0 <= ny < N:
            if not visit[nx][ny] and graph[nx][ny] == "1":
                visit[nx][ny] == True
                count += 1
                
return count 

        
        
            