try:
    num = float(input("enter a number: "))
    if num % 2 == 0:
        print("even number")
    elif num % 2 == 1:
        print("odd number")
    else:
        pass
except(ValueError):
    print("plz only use integers for this")
        
        
