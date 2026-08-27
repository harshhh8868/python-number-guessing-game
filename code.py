#  GUESSING NO. GAME

import random 
a = int(input("initial :"))
b = int(input("final :"))
c = (random.randint (a,b))
while True:
 d = (int(input("guessed no. :")))
 if d > c :
    print("high")
 elif d < c :
    print("low")
 else :d == c  
 print("correct",c)