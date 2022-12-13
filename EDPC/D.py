N ,W=map(int, input().split())
Warr=[]
Varr=[]
for i in range(N):
  w,v = map(int, input().split())
  Warr.append(w)
  Varr.append(v)
dp=[[0]*(W+1)for _ in range(N+1)]
# import sys
# sys.setrecursionlimit(10 ** 7)
# def fdp (i,j):
#   if dp[i][j]!=-1:
#     res= dp[i][j]
#   elif i == N:
#     res= 0
#   elif Warr[i]>j:
#     res= fdp(i+1,j)
#   else:
#     res =max(fdp(i+1,j-Warr[i])+Varr[i],fdp(i+1,j))
#   dp[i][j]=res
#   return res



# print(fdp(0,W))
for i in reversed(range(N)):
  for j in reversed(range(W+1)):
    if Warr[i] > j:
      dp[i][j]=dp[i+1][j]
    else:
      dp[i][j]=max(dp[i+1][j],dp[i+1][j-Warr[i]]+Varr[i])


print(dp[0][W])
