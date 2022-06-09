import sys
from math import gcd
input = sys.stdin.readline

A,B,C = map(int, input().split())
q = gcd(A,B)
y = gcd(B,C)
z = gcd(C,A)
x=min(q,y,z)

print(int(A//x + B//x + C//x-3))