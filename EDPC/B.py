N,K  = map(int, input().split())
h = list(map(int, input().split()))

dp = [10**5]*N
dp[0]= 0
dp[1]= abs(h[0]-h[1])

for i in range(2,N):
  dp[i]=dp[i-1]+abs(h[i-1]-h[i])
  for j in range(2,K+1):
    if i-j >=0:
      dp[i]=min(dp[i],dp[i-j]+abs(h[i-j]-h[i]))

print(dp[N-1])
