import sys
import collections from deque

n = input()
tree = {}

for i in range(n):
    parent,left,right = input().split()
    tree[parent] = (left,right)
    

def preorder(node):
    if node == '.':
        return
    print(node, end = '')
    preorder(tree[node][0])
    preorder(tree[node][1])
    
    
    
    
    
    
def inorder(node):
     if node == '.':
        return
    preorder(tree[node][0])
    print(node, end = '')
    preorder(tree[node][1])
    
    
    
    
    
    


def postorder(node):
     if node == '.':
        return

    preorder(tree[node][0])
    preorder(tree[node][1])
    print(node, end = '')
    
    
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
            