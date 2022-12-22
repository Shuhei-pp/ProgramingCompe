# ベルマンフォードではなくダイクストラ
from collections import deque, defaultdict
N, M, T = map(int, input().split())
que = deque()
TowardGraph, ReturnGraph = defaultdict(list), defaultdict(list)
St = [10**10 for _ in range(N+1)]
Sr = [10**10 for _ in range(N+1)]
A = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, input().split())
    TowardGraph[a].append([b, c])
    ReturnGraph[b].append([a, c])

St[1], Sr[1] = 0, 0

que.append([0, 1])

# 行き
while que:
    p = que.pop()
    fromTime=p[0]
    From =p[1]
    if fromTime > St[From]:
        continue
    for edge in TowardGraph[From]:
        if St[edge[0]] > fromTime+edge[1]:
            St[edge[0]] = fromTime+edge[1]
            que.append([St[edge[0]], edge[0]])


que.append([0, 1])
# 帰り
while que:
    p = que.pop()
    fromTime=p[0]
    From =p[1]
    if fromTime > Sr[From]:
        continue
    for edge in ReturnGraph[From]:
        if Sr[edge[0]] > fromTime+edge[1]:
            Sr[edge[0]] = fromTime+edge[1]
            que.append([Sr[edge[0]], edge[0]])

# 計算
score = [0 for _ in range(N+1)]
for i in range(N):
    score[i] = A[i]*(T-St[i+1]-Sr[i+1])

print(max(score))
