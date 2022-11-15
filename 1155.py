n=int(input())
prior = list(input().split())
P=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
C=
for i in range(6):
    for j in range(2):
        if(prior[i][j]=='A'):
            P[i][j]=0
        elif(prior[i][j]=='B'):
            P[i][j]=1
        else:
            P[i][j]=2
