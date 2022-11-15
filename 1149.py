n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
R=[arr[0][0]]
G=[arr[0][1]]
B=[arr[0][2]]
for i in range(1,n):
    R.append(min(G[i-1],B[i-1])+arr[i][0])
    G.append(min(R[i-1],B[i-1])+arr[i][1])
    B.append(min(R[i-1],G[i-1])+arr[i][2])
print(min(R[n-1],G[n-1],B[n-1]))