try:
    temp = int(input("""
    '1' to convert from Celsius to Fahrenheit or
    '2' to convert from Fahrenheit to Celsius: """))

    def celsius_to_fahrenheit(c):
        return (c * 1.8) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) / 1.8

    if temp == 1:
        celsius = float(input("enter the celsius value that you want to convet: "))
        farenheit = celsius_to_fahrenheit(c)
        print(f'{celsius} is equal to {farenheit}')
    elif temp == 2:
        fahrenheit = float(input("enter the fahrenheit value that you want to convet: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f'{fahrenheit} is equal to {celsius}')
    else:
        print("invalid integer")

except(ValueError):
    print("plz sure to enter the integer only from 1 and 2")
