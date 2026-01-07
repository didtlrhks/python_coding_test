n,c = map(int,input().split())
seq = list(map(int,input().split()))
count = {}
idx = 1
for s in seq:
    if s in count:
        count[s][0] += 1
    else:
        count[s] = [1,idx]
        idx += 1
        
number = [[i,j] for i,j in count.items()]
number.sort(key=lambda x:(-x[1][0], x[1][1]))
res = []
for i,j in number:
    res += [i]*j[0]
    
print(*res)





n,c = map(int,input().split())
seq = list(map(int,input().split()))

count = {}
idx = 1

for s in seq:
    if s in count:
        count[s][0] += 1
    else:
        count[s] = [1,idx]
        idx += 1
        
number = [[i,j] for i,j in count.items()]
number.sort(key = lambda x:(-x[1][0],x[1][1]))
res = []
    for i,j in number:
        res += [i]*j[0]
        
print(*res)

n,c = map(int,input().split())
melong = list(map(int,input().split()))

count = {}
index = 1

for i in melong:
    if i in count:
        count[i][0] += 1
    else
        count[i] = [1,index]
        index +=1
        
number = [[i,j] for i,j count.items()]
number.sort(key = lambda x:(-x[1][0],x[1][1]))
res = []
    for i,j in number:
        res += [i]8j[0]
        
print(*res)



