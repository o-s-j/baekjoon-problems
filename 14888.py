import math
n=int(input())
numbers=list(map(int,input().split()))
how=list(map(int,input().split()))
arr=[]
def every(res,i):
    if(i==n-1):
        arr.append(res)
    else:
        if(how[0]>0):
            how[0]-=1
            every(res+numbers[i+1],i+1)
            how[0]+=1
        if(how[1]>0):
            how[1]-=1
            every(res-numbers[i+1],i+1)
            how[1]+=1
        if(how[2]>0):
            how[2]-=1
            every(res*numbers[i+1],i+1)
            how[2]+=1
        if(how[3]>0):
            how[3]-=1
            every(int(res/numbers[i+1]),i+1)
            how[3]+=1
every(numbers[0],0)
arr.sort()
print(arr[-1])
print(arr[0])
