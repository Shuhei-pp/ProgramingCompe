N  = int(input())
h = list(map(int, input().split()))

c = [10^5]*N
c[0]= 0
c[1]= abs(h[0]-h[1])

for i in range(2,N):
  c[i]=min(c[i-2]+abs(h[i-2]-h[i]),c[i-1]+abs(h[i-1]-h[i]))

print(c[N-1])
