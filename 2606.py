import sys

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
count = 0 





for i in range(M):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    

def DFS(n):
    global count
    visit[n] = True
     
    
     
    for i in graph[n]:
       if not visit[i]:
           count += 1
               
           DFS(i)
           print(count) 


DFS(1)     
           
    
    
    