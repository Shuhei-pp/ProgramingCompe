# import sys
# input = sys.stdin.readline

# N,M =  map(int, input().split())


# def p(x,y,z,A):
#   for i in range(x,y+1):
#     B =A[:]
#     B.append(i)
#     if len(B)==z:
#       print(*B)
#       continue
#     p(i+1,M,z,B)

# A = []
# p(1,M,N,A)

from itertools import combinations

n,m = map(int, input().split())

for l in combinations(range(1, m + 1), n):
    print(*l, sep=' ')