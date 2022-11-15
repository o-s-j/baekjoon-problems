n = int(input())

dp = [0] * (n+1)
dp[0]  = 1
f =1

for i in range(2,n+1):
    f *= i
    f %= 1000000007
    dp[i] = (i-1)*(dp[i-1]+dp[i-2]) % 1000000007
    
print(dp[n]*f % 1000000007)