n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
min=1
max=arr[-1]
while(min<=max):
    mid=(min+max)//2
    total=0
    for i in range(n):
        total+=arr[i]//mid
    if(total>=m):
        min=mid+1
    else:
        max=mid-1
print(max)