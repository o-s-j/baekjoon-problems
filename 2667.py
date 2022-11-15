n=int(input())
arr=[[0]*(n+2)]
num=[]
count=0
apart=0
for i in range(n):
    arr.append([0]+list(map(int,input()))+[0])
arr.append([0]*(n+2))
def dfs(a,b):
    arr[a][b]=0
    global count
    count+=1
    if(arr[a+1][b]==1):
        dfs(a+1,b)
    if(arr[a][b+1]==1):
        dfs(a,b+1)
    if(arr[a-1][b]==1):
        dfs(a-1,b)
    if(arr[a][b-1]==1):
        dfs(a,b-1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if(arr[i][j]==1):
            dfs(i,j)
            num.append(count)
            count=0
print(len(num))
num.sort()
for i in num:
    print(i)

