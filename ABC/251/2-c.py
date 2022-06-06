import sys
input = sys.stdin.readline

n,w= map(int, input().split())
A=list(map(int, input().split()))

c_list=set()
for i,item in enumerate(A):
  if item <= w:
    c_list.add(item)
for i in range(1,n):
  for j in range(i+1,n+1):
    if A[i-1] > w:
      break
    if A[i-1]+A[j-1] <= w:
      c_list.add(A[i-1]+A[j-1])
for i in range(1,n-1):
  for j in range(i+1,n):
    if A[i-1] > w:
      break
    for k in range(j+1,n+1):
      if A[i-1]+A[j-1]+A[k-1] <= w:
        c_list.add(A[i-1]+A[j-1]+A[k-1])
print(len(c_list))
