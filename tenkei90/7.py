import sys
input = sys.stdin.readline

N= int(input())
A = list(map(int, input().split()))
Q = int(input())

def judge(x):
  if len(A)==1:
    return abs(A[0]-x)
  left = 0
  right = N-1
  while right - left> 1:
    mid = int((right + left)/2)
    if A[mid] > x:
      right = mid
    elif A[mid] == x:
      return 0
    else:
      left = mid
  if abs(A[left] - x) - abs(A[left+1] - x)  > 0:
    return abs(A[left+1]-x)
  else:
    return abs(A[left]-x)

A.sort()
for i in range(Q):
  print(judge(int(input())))