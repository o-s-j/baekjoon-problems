n=int(input())
dp=[0 for _ in range(n+1)]
dp[2]=1
dp[3]=1
for i in range(1,n):
    if i*3<=n:
        if(dp[i*3]==0 or dp[i]+1<dp[i*3]):
            dp[i*3]=dp[i]+1
    if i*2<=n:
        if(dp[i*2]==0 or dp[i]+1<dp[i*2]):
            dp[i*2]=dp[i]+1
    if i+1<=n:
        if(dp[i+1]==0 or dp[i]+1<dp[i+1]):
            dp[i+1]=dp[i]+1
print(dp[n])