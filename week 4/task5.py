# Initialize the total to 0
total = 0

# Loop 5 times to get user input
for count in range(5):
    try:
        # Get input from user and convert to a float (to allow decimal numbers)
        number = float(input(f"Enter number {count + 1}: "))
        # Add the entered number to the total
        total += number
    except ValueError:
        print("That's not a valid number. Please enter a numeric value.")

# Print the total
print(f"Total of the numbers entered: {total}")
