n,k=map(int,input().split())
arr=[]
for i in range(n):
  arr.append(input())

arr=arr[0:k]

arr.sort()

for i in arr:
  print(i)
