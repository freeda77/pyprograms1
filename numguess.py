import random
n=5
while n>0:
  a=int(input("enter a number between 0 to 2: "))
  num=random.randrange(0,5)
  if(num==a):
    print("winner")
    break
  else:
    print("try again:")
