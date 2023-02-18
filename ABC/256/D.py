N=int(input())

l,r = map(int,input().split())

arr=[[l,r]]

# nibu
# def judgel(mid,l):
#   if arr[mid][0]<l:
#     return True
#   else:
#     return False

# def judger(mid,r):
#   if arr[mid][1]<r:
#     return True
#   else:
#     return False


for i in range(N-1):
  l,r = map(int,input().split())
  L1=0
  R1=len(arr)
  
  while R1-L1>1:
    mid=int((R1+L1)/2)
    if arr[mid][0]<l:
      L1=mid
    else:
      R1=mid
  if l > arr[L1][0]:
    L1+=1

  L2=0
  R2=len(arr)
  
  while R2-L2>1:
    mid=int((R2+L2)/2)
    if arr[mid][1]<r:
      L2=mid
    else:
      R2=mid

  if r > arr[L2][1]:
    L2+=1

  if L1 != 0:
    if arr[L1-1][1]>=l:
      L1-=1
      l=arr[L1][0]

  if L2 != len(arr):
    if arr[L2][0]<=r:
      r=arr[L2][1]
      L2+=1

  arr[L1:L2]=[[l,r]]
      
for i in arr:
  print(*i)
