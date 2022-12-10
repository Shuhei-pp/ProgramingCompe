



def permutationWithRepetition(n, r):
  return int(pow(n, r))

def permutationWithRepetitionList(data, r):
  length = len(data)
  total = permutationWithRepetition(length, r)
  result = []
  for i in range(total):
    element = []
    for digit in reversed(range(r)):
      element.append(data[int(i / pow(length, digit)) % length])
    result.append(element)
  return result



N,K,D= map(int, input().split())
arr= list(map(int, input().split()))

S=set()

for x in permutationWithRepetitionList(arr,K):
  if(sum(x)%D==0):
    S.add(sum(x))

if len(S)==0:
  print(-1)
else:
  print(max(S))


