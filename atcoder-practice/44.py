import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

N,M = map(int, input().split())
graph=[[]for _ in range(N)]

for i in range(M):
  x,y = map(int, input().split())
  graph[x-1].append(y)
  graph[y-1].append(x)


def dfs(st,graph,times,time):
  times[st-1] = time
  for i in graph[st-1]:
    if times[i-1]==-1 or times[i-1] > time:
      dfs(i,graph,times,time+1)

times = [-1]*N
dfs(1,graph,times,0)
for i in times:
  print(i)  