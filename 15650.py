n,m = list(map(int,input().split()))
 
s = []
def dfs(ind):
    if(len(s)==m):
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(ind+1,n+1):
            if i not in s:
                s.append(i)
                dfs(i)
                s.pop()
dfs(0)