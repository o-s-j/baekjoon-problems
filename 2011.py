num=input()
l=len(num)
arr=[]
dp=[0 for _ in range(l+1)]
for i in range(l):
    arr.append(int(num[i]))
if arr[0]==0:
    print(0)
else:
    arr=[0]+arr
    dp[0]=1
    dp[1]=1
    for i in range(2,l+1):
        if arr[i]>0:
            dp[i]+=dp[i-1]
        tmp=arr[i-1]*10+arr[i]
        if(tmp>=10 and tmp<=26):
            dp[i]+=dp[i-2]
print(dp[l]%1000000)