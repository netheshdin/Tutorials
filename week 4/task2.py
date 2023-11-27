# Initialize variables to store the total score and count of scores entered
total_score = 0
count = 0

while True:
    # Get user input for a score
    try:
        score = float(input("Enter a score (or -9 to stop): "))
        
        # Check if the stopping condition (-9) is met
        if score == -9:
            break
            
        # Update the total score and count
        total_score += score
        count += 1
    except ValueError:
        print("Please enter a valid score or -9 to stop.")

# Calculate and print the average, if any scores were entered
if count > 0:
    average = total_score / count
    print(f"The average of the scores entered is: {average:.2f}")
else:
    print("No scores were entered.")
