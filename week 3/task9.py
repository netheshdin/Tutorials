#small calculator only for the zero division error.
num1 = float(input("Enter any number: "))
op   = input("Enter only '/': ")
num2 = float(input("Enter any number: "))

if op == "/":
    if num2 == 0:
        print("you cant divide a number by 0 ")
    else:
        result = num1 / num2
        print(f'{num1} {op} {num2} = {result}')

else:
    print("You have entered wrong operator")
