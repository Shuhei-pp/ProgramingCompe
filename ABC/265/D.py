N,P,Q,R = map(int, input().split())
arr= list(map(int, input().split()))


k1,k2,k3=0,0,0
v1,v2,v3=0,0,0
for i in range(N):
  while v1 < P and k1 <N:
    v1+= arr[k1]
    v2-=arr[k1]
    k1+= 1
  while v2<Q and  k2 <N:
    v2+= arr[k2]
    v3-=arr[k2]
    k2+= 1
  while v3 < R  and k3 <N:
    v3+= arr[k3]
    k3+= 1
  if v1==P and v2==Q and v3==R:
    print("Yes")
    exit()
  v1 -= arr[i]

print("No")
  

# print("Yes")
