import sys
input = sys.stdin.readline

N,K =  map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max = max(A)
for i in B:
  if max == A[i-1]:
    print("Yes")
    exit()
print("No")