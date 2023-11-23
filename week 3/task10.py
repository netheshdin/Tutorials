#small calculator only for the zero division error.
try:
    num1 = float(input("Enter any number: "))
    op   = input("Enter only '/': ")
    num2 = float(input("Enter any number: "))

    try:
        if op == "/":
            result = num1 / num2
            print(f'{num1} {op} {num2} = {result}')
        else:
            print("you have entered wrong operator")

    except(ZeroDivisionError):
        print("you can not divide numbers by 0")
except(ValueError):
    print("you can only use int values")
