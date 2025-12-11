import sys
from collections import deque

T = int(input())
L = [-1,1,0,0]
H = [0,0,-1,1]
result = []




for _ in range(T):
    M,N,K = map(int,input().split())
    visit = [[False] * M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1
        
    result = 0
      
        
        
   

    def BFS(x,y):
        queue = deque()
        queue.append((x,y))
        visit[y][x] = True
        count = 0
        
        while queue:
            x,y = queue.popleft()
            
            
            for i in range(4):
                nx = x + L[i]
                ny = y + H[i]
            
            
                if 0 <= nx < M and 0 <= ny < N:
                    if not visit[nx][ny] and graph[nx][ny] == 1:
                        queue.append((nx,ny))
                        visit[nx][ny] = True
                
                    
        return 1


    for i in range(N):
        for j in range(M):
            if 0 <= i < M and 0 <= j < N:
                if not visit[i][j] and graph[i][j] == 1:
                    result.append((BFS(i,j)))
                    visit = True
                    []

                        
            
            
        
        

        
        
