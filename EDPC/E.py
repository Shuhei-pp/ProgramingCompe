N ,W=map(int, input().split())
Warr=[]
Varr=[]
for i in range(N):
  w,v = map(int, input().split())
  Warr.append(w)
  Varr.append(v)
dp=[[0]*10100 for _ in range(N+1)]

for i in reversed(range(N)):
  for j in reversed(range(10100)):
    if Varr[i] < j:
      dp[i][j]=dp[i+1][j]
    else:
      dp[i][j]=min(dp[i+1][j],dp[i+1][j-Varr[i]]+Warr[i])


print(dp[0][0:20])
