n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append(b-a)
for k in arr:
    if(k<2):
        print(k)
    else:
        num=2
        i=2
        how=2
        while(num<k):
            num+=i
            how+=1
            if(num<k):
                num+=i
                how+=1
            i+=1
        print(how)


# 1 1
# 2 1 1
# 3 1 1 1
# 4 1 2 1
# 5 1 2 1 1
# 6 1 2 2 1
# 7 1 2 2 1 1
# 8 1 2 2 2 1
# 9 1 2 3 2 1
# 10 1 2 3 2 1 1
# 11 1 2 3 2 2 1
# 12 1 2 3 3 2 1
# 13 1 2 3 3 2 1 1
# 14 1 2 3 3 2 2 1
# 15 1 2 3 3 3 2 1
# 16 1 2 3 4 3 2 1
# 17 1 2 3 4 3 2 1 1
# 18 1 2 3 4 3 2 2 1
# 19 1 2 3 4 3 3 2 1
# 20 1 2 3 4 4 3 2 1