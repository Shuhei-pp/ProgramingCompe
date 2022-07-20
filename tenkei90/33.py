import sys
input = sys.stdin.readline

H,W = map(int, input().split())
if H == 1 or W ==1:
  print(H*W)
  exit()
if H%2 == 1:
  H += 1
if W % 2 == 1:
  W += 1


print(int(H/2*W/2))