integer_1 = float(input("enter a number: "))
operator  = input("enter an operator you want: ")
integer_2 = float(input("enter a number: "))

def calculator(num_1, operator, num_2):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        if num_2 == 0:
            return "Error"
        else:
            return num_1 / num_2
    else:
        return "invalid operator"

result = calculator(integer_1, operator, integer_2)

print(f'{integer_1} {operator} {integer_2} = {result}')
    
