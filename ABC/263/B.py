import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))


i=len(A)
c=1
while True:
  if 1 == A[i-1]:
    print(c)
    exit()
  i = A[i-1]-1
  c+=1