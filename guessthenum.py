# the computer chooses 1 random number between 1 and 100
import random
num = random.randint(0,101)
# ask the user to guess the number
inp = int(input("Guess the number! "))

#guide the user to the answer
while(num != inp):
    
    if( inp < num):
        print("the number is higher")
    else:
        print("the number is lower")
    
    inp = int(input('enter another number'))

print("yes the number is", inp)


