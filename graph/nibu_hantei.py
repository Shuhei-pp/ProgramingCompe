N,M=map(int,input().split())
from collections import defaultdict
graph=defaultdict(list)
color=[0 for _ in range(N+1)]

for i in range(M):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# 2部グラフか判定する
def dfs(i,c):
  color[i]=c
  for item in graph[i]:
    if c == color[item]:
      return False
    if color[item]==0:
      color[item]=-c
      if not dfs(item,-c):
        return False
  return True
    
    
for i in range(1,N+1):
  if color[i]==0:
    if not dfs(i,1):
      print("No")
      exit()

print("Yes")

