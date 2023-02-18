N,M = map(int, input().split())
from collections import defaultdict
graph=defaultdict(int)
for i in range(M):
  u,v = map(int, input().split())
  graph[u]=v
  graph[v]=u


def dfs(st,graph,visited):
  visited[st-1]=1
  for i in graph[st-1]:
    if visited[i-1]!=1:
      dfs(i,graph,visited)

visited = [0]*N
dfs(1,graph,visited)
