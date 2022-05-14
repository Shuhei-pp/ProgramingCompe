n,w= map(int, input().split())
A=list(map(int, input().split()))
c_list=[]
for i,item in enumerate(A):
  if item <= w:
    if not item in c_list:
      c_list.append(item)

for i in range(1,n):
  for j in range(i+1,n+1):
    if A[i-1]+A[j-1] <= w:
      if not A[i-1]+A[j-1] in c_list:
        c_list.append(A[i-1]+A[j-1])
for i in range(1,n-1):
  for j in range(i+1,n):
    for k in range(j+1,n+1):
      if A[i-1]+A[j-1]+A[k-1] <= w:
        if not A[i-1]+A[j-1]+A[k-1] in c_list:
          c_list.append(A[i-1]+A[j-1]+A[k-1])
print(len(c_list))
