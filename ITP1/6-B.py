n= int(input())
cards = []
for i in range(n):
  card = input()
  cards.append(card)

marks = ["S","H","C","D"]
for i,mark in enumerate(marks):
  for j in range(13):
    # for k,card in enumerate(cards):
    k = 0
    while True:
      card_tmp = mark+" "+str(j+1)
      if len(cards) == k:
        print(card_tmp)
        break
      if cards[k] == card_tmp:
        break
      k += 1

