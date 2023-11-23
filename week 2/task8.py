n = input("please enter an integer: ")
try:
    n = int(n)
    print(n)

except ValueError:
    print("Requires a valid integer")


x = float(input("Enter the number: "))
y = float(input("Enter the number that you want to divide: "))

try:
    z = x / y
    print(z)

except ZeroDivisionError:
    print("0 is not a valid number")
