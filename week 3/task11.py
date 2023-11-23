import random

# Generate a random number: 0 or 1
flip_result = random.randint(0, 1)

# Check the result and print accordingly
if flip_result == 0:
    print('Heads')
else:
    print('Tails')
