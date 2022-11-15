n, m=map(int,input().split())
arr=[[0]*(m+2) for i in range(n+2)]
for i in range(1,n+1):
  temp=input()
  for j in range(1,m+1):
    arr[i][j]=int(temp[j-1])
kimo=[]
def bsf(p,a,b,count):
  p[a][b]=0
  if a==n and b==m:
    kimo.append(count)
  else:
    count+=1
    if(p[a+1][b]==1):
      bsf(p,a+1,b,count)
    if(p[a-1][b]==1):
      bsf(p,a-1,b,count)
    if(p[a][b+1]==1):
      bsf(p,a,b+1,count)
    if(p[a][b-1]==1):
      p(arr,a,b-1,count)
bsf(arr,1,1,1)
print(kimo)