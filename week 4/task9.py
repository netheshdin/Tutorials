import random

max_guesses = 5
secret_num = random.randint(1,20)

def guess_the_number():
    for attempt in range(1, max_guesses + 1):
        try:
            guess = int(input("Guess the number between 1 and 20: "))

            if guess == secret_num:
                print(f'congratulations! You guessed the correct number in {attempt} attempts')
                break
            
            else:
                if guess < secret_num:
                    print('try again. the correct number is high. ')
                else:
                    print('try again. the correct number is lower. ')
        except ValueError:
            print("You can only use integers ")

    else:
        print(f'sorry you have run out of attempts. The correct number was {secret_num}')

guess_the_number()
