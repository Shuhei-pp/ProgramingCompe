n, l, r = map(int, input().split())
A = list(map(int, input().split()))
B=[]

for i in range(n):
    if i ==0:
        B.append(min(A[0],l*(i+1)))
    else:
        B.append(min(B[i-1]+A[i],l*(i+1)/(i+1)))

lIndex=max([i for i,v in enumerate(B) if v == min(B)])


for i,v in enumerate(A):
    if i <= lIndex:
        A[i]=l

print(A,B)

C=[]
# 右！！
A.reverse()
for i in range(n):
    if r*(i+1) > sum(A[0:i+1]):
        C.append(sum(A[0:i+1])/(i+1))
    else:
        C.append(r)

rIndex=max([i for i,v in enumerate(C) if v == min(C)])


for i,v in enumerate(A):
    if i <= rIndex:
        A[i]=r

print(A,C)




