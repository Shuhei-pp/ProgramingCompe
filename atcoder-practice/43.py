import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

N,M = map(int, input().split())
graph=[[]for _ in range(N)]

for i in range(M):
  x,y = map(int, input().split())
  graph[x-1].append(y)
  graph[y-1].append(x)

def dfs(st,graph,visited):
  visited[st-1]=1
  for i in graph[st-1]:
    if visited[i-1]!=1:
      dfs(i,graph,visited)

visited = [0]*N
dfs(1,graph,visited)

if not 0 in visited:
  print("The graph is connected.")
  exit()

print("The graph is not connected.")