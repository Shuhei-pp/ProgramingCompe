N= int(input())

a,b,c = map(int, input().split())
H=[[a,b,c]]
for i in range(N-1):
  a,b,c = map(int, input().split())
  newarr=[max(H[i][1],H[i][2])+a,max(H[i][0],H[i][2])+b,max(H[i][0],H[i][1])+c]
  H.append(newarr)

print(max(H[N-1]))