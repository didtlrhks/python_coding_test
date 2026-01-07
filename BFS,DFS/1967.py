import sys
import collections from deque

input = sys.stdin.readline


n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1):
    parent,child,weight = map(int,input().split())
    tree[parent].append((child,weight))
    tree[child].append((parent,weight))
    

visit = [False] * (n+1)
max_tree = 0
farthest_node = 1

def DFS(node,tree):
    global max_tree, farthest_node
    visit[node] = True
    
    if tree > max_tree:
        max_tree = tree
        farthest_node = node   
    
    for next_node,weight in tree[node]:
        if not visit[next_node]:
            dfs(next_node,tree + weight)
            
DFS(1,0)

visit = [False] * (n+1)
max_tree = 0

DFS(farthest_node,0)

print(max_tree)