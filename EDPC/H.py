H,W = map(int, input().split())

G=[]
for i in range(H):
  width=list(input())
  G.append(width)

count=[[0 for p in range(W)]for _ in range(H)]

for h in range(H):
  for w in range(W):
    if G[h][w]=="#":
      continue
    if h==0 and w== 0:
      count[h][w]=1
    elif  h==0:
      count[h][w]=count[h][w-1]
    elif  w==0:
      count[h][w]=count[h-1][w]
    else:
      count[h][w]=count[h-1][w]+count[h][w-1]
    


print(count[H-1][W-1]%(10**9+7))
