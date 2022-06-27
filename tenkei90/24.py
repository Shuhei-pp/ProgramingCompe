import sys
input = sys.stdin.readline

n,k=  map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = 0

for i in range(n):
  diff += abs(A[i]-B[i])

if (k -diff)%2 == 0 and diff <= k:
  print("Yes")
else:
  print("No")
