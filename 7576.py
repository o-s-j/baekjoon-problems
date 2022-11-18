from collections import deque #bfs 사용할 때에는 queue 써줘야함 popleft() O(1) pop(0) O(n)이라서
m,n=map(int,input().split())
arr=[[-1]*(m+2)]
for i in range(n):
    arr.append([-1]+list(map(int,input().split()))+[-1])
arr.append([-1]*(m+2))
rare=0
well=deque([])
for i in range(1,n+1):
    for j in range(1,m+1):
        if(arr[i][j]==0):
            rare+=1
        elif(arr[i][j]==1):
            well.append([i,j])
count=0
day=0
l=len(well)
tried=0
while((well) and rare!=0):
    p=well.popleft()
    tried+=1
    if(arr[p[0]+1][p[1]]==0):
        arr[p[0]+1][p[1]]=1
        well.append([p[0]+1,p[1]])
        count+=1
    if(arr[p[0]-1][p[1]]==0):
        arr[p[0]-1][p[1]]=1
        well.append([p[0]-1,p[1]])
        count+=1

    if(arr[p[0]][p[1]-1]==0):
        arr[p[0]][p[1]-1]=1
        well.append([p[0],p[1]-1])
        count+=1

    if(arr[p[0]][p[1]+1]==0):
        arr[p[0]][p[1]+1]=1
        well.append([p[0],p[1]+1])
        count+=1

    if(tried==l):
        l=len(well)
        tried=0
        day+=1

if(rare==0):
    print(0)
elif(count==rare):
    print(day-1)
else:
    print(-1)