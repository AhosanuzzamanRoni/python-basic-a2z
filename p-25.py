from random import randint
for x in range(1,101):
  guessnumber=int(input("Enter your guess between 1 to 100:"))
  randomnumber = randint(1,100)
  if guessnumber == randomnumber:
    print("you have win")
  else:


    print("you have lost")
    print( randomnumber)
