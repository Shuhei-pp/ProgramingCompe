import sys
input = sys.stdin.readline

Y = int(input())

if Y%4 <= 2:
  print(Y-(Y%4)+2)
  exit()

print(Y-(Y%4)+6)

