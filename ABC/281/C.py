N,T =  map(int, input().split())
arr = list(map(int, input().split()))

e = T%sum(arr)

for i,item in enumerate(arr):
  e -= item
  if e <= 0:
    print(i+1,e+item)
    exit()

