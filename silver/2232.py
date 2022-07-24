a=[]
res=[]
idx=0
num=int(input())
for i in range(num):
    n=int(input())
    a.append(n)
while idx<num:
    if(idx==num-1):
        res.append(idx+1)
    elif(a[idx]>=a[idx+1]):
        res.append(idx+1)
        while(idx!=num-1):
            if(a[idx]>a[idx+1]):
                idx+=1
            else:
                break
    idx=idx+1
for j in res:
    print(j)