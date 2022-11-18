n=int(input())
arr=[[0]*n for _ in range(n)]
count=0
def dfs(i,j):
    global count,arr
    if(arr[i][j]==0):
        if i==n-1:
            count+=1
            if(j<n-1):
                dfs(i,j+1)
        else:    
            temp=arr
            for k in range(n):
                if(i+abs(k-j)<n):
                    arr[i+abs(k-j)][k]=1
                arr[k][j]=1
            dfs(i+1,0)
            arr=temp
            if(j<n-1):
                dfs(i,j+1)
    else:
        if(j<n-1):
            arr[i][j-1]
dfs(0,0)
print(count)