

N,M,V = map(int,input().split())


graph = [[] for _ in range(N+1)]


for _ in range(M):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    

for i in range(1,N+1):
    graph[i].sort()
    
visit = [False] * (N + 1)

def DFS(v):
    visited[v] = True
    print(v,end= ' ')
    
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
            
DFS(V)            