n,bag=map(int,input().split())
value=[0]*(bag+1)
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
def max_bag(v,i,p,cur,val):
    if(i<n):
        hi=cur+arr[i][0]
        if(p==1):
            if(hi<=bag):
                val+=arr[i][1]
                if(value[hi]<val):
                    value[hi]=val
                    max_bag(v,i+1,0,hi,val)
                    max_bag(v,i+1,1,hi,val)
                else:
                    max_bag(v,i+1,0,hi,val)
                    max_bag(v,i+1,1,hi,val)
            else:
                max_bag(v,i+1,0,cur,val)
                max_bag(v,i+1,1,cur,val)
        else:
            max_bag(v,i+1,0,cur,val)
            max_bag(v,i+1,1,cur,val)
            
max_bag(bag,0,0,0,0)
max_bag(bag,0,1,0,0)
for i in range(1,bag+1):
    if(value[i]==0 or value[i]<value[i-1]):
        value[i]=value[i-1]
print(value[bag])