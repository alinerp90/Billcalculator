#Build a calculator to find out how much each person should pay equally in a bill considering the tip

print("Welcome to the calculator!")
bill = float(input("How much was the bill?"))
tip = int(input("How much percent you want to tip?"))
people = int(input("How many people wants to split the bill?"))

p_tip = 1 + tip/100 #% tip
p_bill = bill * p_tip #total with tip
total = p_bill / people #total per person

#Format the result to 2 decimal places
final_total = round(total, 2)
print(f"Each person should pay: {final_total}")

