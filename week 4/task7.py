# Ask the user for the number of stars
try:
    num_stars = int(input("How many stars (*) are required? "))

    for i in range(1, num_stars + 1):
        print("*" * i)

except ValueError:
    print("Please enter a valid integer.")
