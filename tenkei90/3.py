import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
arr = [[]for _ in range(N+1)]

for i in range(N-1):
  a,b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

distance = [0 for i in range(N+1)]

def dfs(now,bef,dist):
  distance[now] = dist
  for next in arr[now]:
    if next != bef:
      dfs(next,now,dist+1)

dfs(1,-1,0)

max_place = 0
max_dis = max(distance)
for i,item in enumerate(distance):
  if item == max_dis:
    max_place = i
    break

distance = [0] *(N+1)
dfs(max_place,-1,0)

print(max(distance)+1)
