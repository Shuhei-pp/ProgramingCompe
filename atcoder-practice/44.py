import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

N,M = map(int, input().split())
graph=[[]for _ in range(N+1)]

for i in range(M):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

que = deque()
times = [-1]*(N+1)
times[1]=0

que.append(1)

while que:
  i = que.popleft()
  for _ in graph[i]:
    if times[_] == -1:
      times[_] = times[i]+1
      que.append(_)


for i in times[1:]:
  print(i)  