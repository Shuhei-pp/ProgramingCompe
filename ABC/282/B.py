N,M = map(int, input().split())
S=[]
for i in range(N):
  S.append(list(input()))
count=0
for i in range(N-1):
  for j in range(i+1,N):
    for k in range(M):
      if (S[i][k]=="o" or S[j][k]=="o") and k==M-1:
        count+=1
        continue
      if S[i][k]=="x" and S[j][k]=="x":
        break
    

print(count)
