# # Print the title
# print("Welcome to the Tip Caculator!")
# # Variable naming
# bill = float(input("How much the total bill?\n"))
# tip = int(input("How much tip would you like to give? 5, 10 or 15?\n"))
# people = int(input("How many people to split the bill\n"))
# tip_as_percent = tip / 100
# # caculate
# total_tip__amount = bill * tip_as_percent
# total_bill = total_tip__amount + bill
# bill_per_person = total_bill / people
# # Round the amount to 2 units
# final_pay = round(bill_per_person, 2)
# # Print result
# print(f"Each person should pay ${final_pay}")