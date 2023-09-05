print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10,20, or 15? "))
total_people = int(input("How many people to split the bill?"))
new_bill = total_bill + tip_percentage/100 * total_bill
final = "{:.2f}".format(round(new_bill/total_people,2))
print(f"Each person should pay: ${final}")
