n = int(input())
list = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
for i in range(n):
  b,f,r,v = map(int, input().split())
  list[b-1][f-1][r-1] += v
for i,building in enumerate(list):
  for floor in building:
    print(" ",end="")
    print(*floor)
  if i != 3:
    print("####################")