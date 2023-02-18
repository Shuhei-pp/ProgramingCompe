
N, M, T = map(int, input().split())
TowardGraph, ReturnGraph = [], []
St = [10**10 for _ in range(N+1)]
Sr = [10**10 for _ in range(N+1)]
A = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, input().split())
    TowardGraph.append([a, b, c])
    ReturnGraph.append([b, a, c])

St[1], Sr[1] = 0, 0

# 行き
while True:
    update = False
    for edge in TowardGraph:
        if St[edge[0]] != 10**10 and St[edge[1]] > St[edge[0]]+edge[2]:
            St[edge[1]] = St[edge[0]]+edge[2]
            update = True
    if not update:
        break

# 帰り
while True:
    update = False
    for edge in ReturnGraph:
        if Sr[edge[0]] != 10**10 and Sr[edge[1]] > Sr[edge[0]]+edge[2]:
            Sr[edge[1]] = Sr[edge[0]]+edge[2]
            update = True
    if not update:
        break

# 計算
score = [0 for _ in range(N+1)]
for i in range(N):
    score[i] = A[i]*(T-St[i+1]-Sr[i+1])

print(max(score))
