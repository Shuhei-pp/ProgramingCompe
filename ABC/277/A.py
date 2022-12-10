N,X =  map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N):
  if X==arr[i]:
    print(i+1)
    exit()
