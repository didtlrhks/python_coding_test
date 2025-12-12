import sys
import sys.setrecursionlimit(2000)

input = sys.stdin.readline

N,M = map(int,input().split())
visit = [False] * (N+1)
graph = [[] for _ in range(N+1)]
count = 0



for i in range(M):
    u,v = map(int,input().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
    

def DFS(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            DFS(i)
            

for i in range(1,N+1):
    if not visit[i]:
        DFS(i)
        count += 1
        
print(count)
    
    
    
            
    
            
        
        
    
    
    
    