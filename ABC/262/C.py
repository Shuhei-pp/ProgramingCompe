import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
c_count = 0
e_count = 0
for i in range(N):
  if i+1 == A[i]:
    c_count+= 1
  else:
    # print(i)
    if A[i] > i+1 and A[A[i]-1] == i+1:
      e_count+= 1

re =0
for i in range(1,c_count):
  re += i

print (int(re+e_count))


