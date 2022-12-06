H,W = map(int, input().split())

G=[]
for i in range(H):
  biside = input()
  G.append(list(biside))

i=0
j=0
wall=0
while True:
  if G[i][j]=="U":
    i=i-1
    if i == -1:
      print(i+2,j+1)
      exit()
  elif G[i][j]=="D":
    i=i+1
    if i == H:
      print(i,j+1)
      exit()
  elif G[i][j]=="L":
    j=j-1
    if j == -1:
      print(i+1,j+2)
      exit()
  elif G[i][j]=="R":
    j=j+1
    if j == W:
      print(i+1,j)
      exit()
  wall= wall+1
  if(wall>W*H+10):
    print(-1)
    exit()


# print("Yes")
