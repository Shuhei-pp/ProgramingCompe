s=input()
t= input()

lt,ls=len(t),len(s)

dp=[["" for i in range(ls+1)] for _ in range(lt+1)]

for i in range(lt):
  for j in range(ls):
    if t[i]==s[j]:
      dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j], dp[i][j]+t[i], key=len)
    else:
      dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

# print(dp)
print(dp[lt][ls])