""" This is a simple calculator that takes total expense as input then asks how much they want to tip and finally
ask numbers of persons they want to split that amount then return output"""

print("Welcome to the Tip Calculator")  # Welcome message

totalBill = float(input("What was the total Bill?  Rs."))  # This will ask and takes total bill as input

tip = int(input("What percentage of tips would you like to give 10, 12 or 15 "))  # This will ask for the tip amount

tipAmount = (totalBill * tip) / 100  # This will calculate the  total tip  based on tip percentages

totalPerson = int(input("How many people to split the bill? "))  # This will ask how many person involved

totalSplit = tipAmount / totalPerson  # This will calculate each person's share
totalSplitAmount = "{:.2f}".format(totalSplit)

print(f"Each person should pay Rs. {totalSplitAmount}")  # Final result
