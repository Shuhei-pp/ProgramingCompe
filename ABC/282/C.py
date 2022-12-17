N = int(input())
S=list(input())

c=True
for i in range(N):
  if S[i]=="\"":
    c=not c
  elif S[i]==",":
    if c:
      S[i]="."

print("".join(S))
