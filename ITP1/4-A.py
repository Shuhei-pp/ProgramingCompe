import math
a,b = map(int, input().split())
d = math.floor(a/b)
r = math.floor(a%b)
print(d,r,'{:.05f}'.format(a/b))