n,m = map(int, input().split())
A,B = [],[]
for i in range(n):
  A.append(list(map(int, input().split())))
for i in range(m):
  B.append(int(input()))
for i in range(n):
  x = 0
  for index,val in enumerate(A[i]):
    x += val * B[index]
  print(x)

