N,M = map(int, input().split())
from  collections import defaultdict,deque
import sys
sys.setrecursionlimit(10 **7)
graph =defaultdict(list)

for i in range(M):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
path=deque()
def dfs(start,route):
  route.append(start)
  if len(route)==N:
    return 1
  count= 0
  for i in graph[start]:
    if i not in route:
      count+=dfs(i,route)
      path.pop()
  return count

print(dfs(1,path))
