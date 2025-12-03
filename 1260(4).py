import sys

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for i in range(1,N+1):
    S,E = map(int,input().split())
    graph[S].append(E)
    graph[E].append(S)
    
    
for i in range(1,N+1):
    graph[i].sort



def DFS(v):
    visit[v] = True
    print(v,end = " ")
    for i in graph[v]:
        if not visit[i]:
            DFS(i)
            
DFS(V)