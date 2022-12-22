# 最短路問題,ベルマンフォード問題
# 負の閉路が存在する場合もある
N,M=map(int,input().split())
graph=[]
Sp=[10**9 for _ in range(N+1)]

for i in range(M):
  a,b,c=map(int,input().split())
  graph.append([a,b,c])
  graph.append([b,a,c])

Sp[1]=0

while True:
  update=False
  for edge in graph:
    if Sp[edge[0]]!=10**9 and Sp[edge[1]] > Sp[edge[0]]+edge[2]:
      Sp[edge[1]]=Sp[edge[0]]+edge[2]
      update=True
  if not update:
    break

print(*Sp)