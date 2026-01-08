import sys

input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    s = input().strip()
    cmd = s.split()
    # slice 뭔가를 해야할듯?
    
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    
    elif cmd[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif cmd[0] == "size":
        print(len(stack))
    
    elif cmd[0] == "empty":
        print(0 if stack else 1)
        
    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
        