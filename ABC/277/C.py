N= int(input())

from collections import defaultdict,deque
graph=defaultdict(list)
for i in range(N):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

que= deque()
que.append(1)
end = set()
end.add(1)


while que:
  currnt = que.popleft()
  for v in graph[currnt]:
    if not v in end:
      end.add(v)
      que.append(v)

print(max(end))
