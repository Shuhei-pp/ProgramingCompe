N,M = map(int, input().split())
from  collections import defaultdict
import sys
sys.setrecursionlimit(10 **6)
graph =defaultdict(list)
start=[True]*(N+1)
for i in range(M):
  a,b= map(int, input().split())
  graph[a].append(b)
  start[b]=False

l=[0]*(N+1)
visited=[False]*(N+1)

def dfs(r):
  if visited[r]:
    return l[r]
  for item in graph[r]:
    l[r]=max(l[r],dfs(item)+1)
    visited[item]=True
  return l[r]


for i in range(1,N+1):
  if start[i]:
    dfs(i)

print(max(l))



