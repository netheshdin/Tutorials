total_cost = float(input("enter the cost of the meal: "))

rating = int(input("""

****Rate your satisfaction level****
1 = Totally satisfied
2 = Satisfied
3 = Dissatisfied
Enter your rating (1, 2, or 3): """))

if rating == 1:
    tip_percentage = 20
    tip = total_cost * (tip_percentage / 100)
    full_amount = total_cost + tip
    satisfacation_level = "Totally satisfied"
    
elif rating == 2:
    tip_percentage = 15
    tip = total_cost * (tip_percentage / 100)
    full_amount = total_cost + tip
    satisfacation_level = "satisfied"

elif rating == 3:
    tip_percentage = 10
    tip = total_cost * (tip_percentage / 100)
    full_amount = total_cost + tip
    satisfacation_level = "dissatisfied"

else:
    print("invalid rating entered: ")

print(f"satisfacation level: {satisfacation_level}")
print(f"suggest tip        : {tip}")
print(f"full amount        : {full_amount}")
