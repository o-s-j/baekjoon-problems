n,bag=map(int,input().split())
value=[0]*(bag+1)
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
for i in range(n-1):
    if(arr[i][0]==arr[i+1][0]):
        if(arr[i][1]>arr[i+1][1]):
            arr.pop(i+1)
        else:
            arr.pop(i)
arr.sort()
for i in range(len(arr)):
    if(arr[i][0]<bag):
        value[arr[i][0]]=arr[i][1]
for i in range(1,bag+1):
    if(value[i]==0):
        value[i]=value[i-1]
    else:
        for j in range(len(arr)):
            if i+arr[j][0]<=bag:
                if(value[i]+arr[j][1]>value[i+arr[j][0]]):
                    value[i+arr[j][0]]=value[i]+arr[j][1]
print(value[bag])