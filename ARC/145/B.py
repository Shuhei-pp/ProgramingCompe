import sys
input = sys.stdin.readline

N,A,B = map(int, input().split())

# for i in range(1,N+1):
#   if A <= i:
#     if B > i%A:
#       ac += 1

if A > N:
  print(0)
  exit()

if A <= B:
  print(int(N-A+1))
  exit()

if N%A < B:
  print(int((N//A-1)*B + N%A + 1)) 
  exit()

print(int((N//A)*B))



