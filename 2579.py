ans=[]
def Max_Num(arr,total,bef,i):
    if(i==len(arr)-1):
        total+=arr[i]
        ans.append(total)
    if(i>=len(arr)):
        return 0
    if(bef==2):
        total+=arr[i]
        Max_Num(arr,total,2,i+2)
        Max_Num(arr,total,1,i+1)
    else:
        total+=arr[i]
        Max_Num(arr,total,2,i+2)

        
num=int(input())
arr=[]
for i in range(num):
    arr.append(int(input()))
arr.reverse()
total=0
Max_Num(arr,total,2,0)
ans.sort()
print(ans[-1])