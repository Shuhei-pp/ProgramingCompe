import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1
  graph[b-1][a-1] = 1  # 有向グラフなら消す
c = 0
for i in range(n):
  for j in range(n):
    for k in range(n):
      if graph[i][j] == 1 and graph[j][k] == 1 and graph[k][i]==1 and i < j < k:
        c += 1

print(c)
