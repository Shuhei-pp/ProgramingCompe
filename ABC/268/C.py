N= int(input())
P= list(map(int, input().split()))
counts=[0 for i in range(N)]

for i in range(N):
  if P[i]-i+1 == N:
    counts[P[i]-i-1]+=1
    counts[P[i]-i]+=1
    counts[0]+=1
  else:
    counts[P[i]-i-1]+=1
    counts[P[i]-i]+=1
    counts[P[i]-i+1]+=1



print(max(counts))

