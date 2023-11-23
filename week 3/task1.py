try:
    age = int(input("enter your age: "))
    if age >= 18:
        print("you can vote")
    else:
        print("you can not vote")
        
except(ValueError):
    print("You can enter only integer values")
