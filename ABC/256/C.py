a,b,c,d,e,f=map(int,input().split())
count=0

for i in range(1,a-1):
  for j in range(1,a-i):
    for k in range(1,b-1):
      for ii in range(1,b-k):
        if i+k<d and j+ii<e and ((a-i-j)+(b-k-ii))<f and (d-(i+k)) + (e-(j+ii))+f-((a-i-j)+(b-k-ii))==c:
          count+=1
print(count)

