x,y,N = map(int, input().split())

if N < 3:
  print(x*N)
elif y<=3*x :
  print(y*int(N/3)+x*(N%3))
elif y>3*x :
  print(x*(N))
