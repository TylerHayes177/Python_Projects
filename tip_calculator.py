print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = int(tip)
tip_decimal = tip_percentage / 100

print(f"Each person should pay {(bill * tip_decimal) / people}")
