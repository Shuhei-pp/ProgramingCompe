N,M = map(int, input().split())
from collections import defaultdict
graph=defaultdict(list)
for i in range(M):
  u,v = map(int, input().split())
  graph[u]=v
  graph[v]=u

# // 長さ3以上の辺を見つける!
count=0

visited=[False]*(N+1)

def dfs(r):
  if visited[r]:
    return l[r]
  for item in graph[r]:
    # l[r]=max(l[r],dfs(item)+1)
    visited[item]=True
  return l[r]


for i in range(1,N+1):
  if start[i]:
    dfs(i)
print(count)