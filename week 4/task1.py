import random

hide = random.randint(1,20)

num = int(input("enter a number 1 - 20: "))

while num != hide:
    if num < hide:
        print(num, "is too low.")
    else:
        print(num, "is too high.")
    num = int(input("enter a number 1 - 20: "))

print(num, "it is correct.")
    
          
          
