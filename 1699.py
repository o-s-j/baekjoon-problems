import math
n=int(input())
k=0
while(pow(k+1,2)<=n):
    k+=1
arr=[0]*(n+1)
for i in range(1,k+1):
    arr[i*i]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        p=i+(j*j)
        if(p<=n):
            if(arr[p]==0 or arr[p]>arr[i]+1):
                arr[p]=arr[i]+1
        else:
            break
print(arr[n])
#좋은 예시
# n = int(input())
# d=[0,1,2,3,1]

# for i in range(5,n+1):
#     root = int(i**(1/2))
#     d.append(d[i-1]+1)
#     for j in range(2,root+1):
#         d[i] = min(d[i],d[i-j*j]+1)
# print(d[n])