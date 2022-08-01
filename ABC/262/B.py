import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)  # 有向グラフなら消す

# q=[]
# for i in range(N):
#   q[0]=i-1
#   for j in range(N):

print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]

