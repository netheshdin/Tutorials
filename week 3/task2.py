try:
    x = int(input("Give me a number: "))
    if x < 0:
        print(x, "is negative")
    else:
        print(x, "is positive")

except:
    print("enter only a number. ")

