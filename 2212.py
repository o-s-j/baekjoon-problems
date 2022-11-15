import sys
N=int(input())
K=int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
dist=[]
if K>=N:
    print(0)
    sys.exit()
for i in range(1,N):
    dist.append(arr[i]-arr[i-1])
dist.sort(reverse=True)
for _ in range(K-1):
    dist.pop(0)
print(sum(dist))