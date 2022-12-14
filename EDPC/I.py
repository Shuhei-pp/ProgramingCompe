N= int(input())

A=list(map(float, input().split()))

dp=[[0 for p in range(N+1)]for _ in range(N+1)]

dp[0][0]=100
for i in range(N):
  dp[0][i+1]=dp[0][i]*(1-A[i])

for i in range(1,N+1):
  for j in range(1,N+1):
    if i>j:
      continue
    else:
      dp[i][j]= dp[i-1][j-1]*A[j-1]+dp[i][j-1]*(1-A[j-1])

p=0
for i,item in enumerate(dp):
  if N/2 > i:
    continue
  p+=item[N]

print(p/100)
