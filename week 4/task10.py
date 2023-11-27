import random
max_guesses = 3
fruits = ['apple', 'banana', 'orange', 'lemon']
choice = random.choice(fruits)

for attempt in range(1, 4):
    print("""---This is a game---

***You have four fruits***
1.Apple
2.Banana
3.orange
4.lemon

You have only 3 attempts to do this..... you have to choose the correct fruit
that have chosen by the computer..""")
    print()
    guess = str(input("Enter the fruit name that you think: ")).lower()
    if guess == choice:
                print(f'congratz!!! You have chosen the correct fruit name in {attempt} attempts.')
                break
    else:
        print("You have chosen wrong fruit name")
else:
    print("You could not do this")

                
