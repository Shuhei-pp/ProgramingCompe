import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())

if a == 1:
  if b==1:
    print(c)
  else:
    print(d)
else:
  if b==1:
    print(e)
  else:
    print(f)
