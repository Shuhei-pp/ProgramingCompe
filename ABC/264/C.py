
h1,w1 = map(int, input().split())
A=[]
for i in range(h1):
    arr=list(map(int, input().split()))
    A.append(arr)

h2,w2 = map(int, input().split())
B=[]
for i in range(h2):
    arr=list(map(int, input().split()))
    B.append(arr)

print(A,B)


from itertools import combinations


for i in combinations(A,h2):
    print(*i)