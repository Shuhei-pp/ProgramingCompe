room,bonus,time = map(int, input().split())
times= list(map(int, input().split()))

for i in range(bonus):
  Broom,Btime = map(int, input().split())
  times[Broom-1]=times[Broom-1]-Btime

for i in range(room-1):
  time= time-times[i]
  if time <= 0:
    print("No")
    exit()

print("Yes")
