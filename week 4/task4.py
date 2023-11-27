while True:
    n = input("Please enter an integer: ")
    try:
        n = int(n)
        break  # This will break out of the loop once a valid integer is provided.
    except ValueError:
        print("Requires a valid integer! Please try again.")

print("You successfully entered an integer.")
