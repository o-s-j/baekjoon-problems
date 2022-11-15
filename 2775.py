arr=[[i for i in range(15)]]
for i in range(14):
    arr.append([0]*15)
for i in range(1,15):
    for j in range(1,15):
        arr[i][j]=arr[i-1][j]+arr[i][j-1]
ans=[]
t=int(input())
for _ in range(t):
    n=int(input())
    k=int(input())
    ans.append([n,k])
for i in range(t):
    print(arr[ans[i][0]][ans[i][1]])