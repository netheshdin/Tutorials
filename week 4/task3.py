total = 0
count = 0
try:
    score = float(input("enter score, (Enter -9 to end): "))

    while score != -9:
        total = total + score
        count = count + 1
        score = float(input("enter score, (Enter -9 to end): "))

    if count == 0:
        print("No scores were entered")
    else:
        average = total / count
        print(f'average is {average} ')
except(ValueError):
    print("only integers you can put!!")
