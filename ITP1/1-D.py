x = int(input())
h = int(x / 3600)
m = int((x % 3600)/60)
s = (x % 3600)%60
print(str(h)+":"+str(m)+":"+str(s))