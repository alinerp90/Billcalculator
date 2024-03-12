#Build a calculator to find out how much each person should pay equally in a bill considering the tip

print("Welcome to the calculator!")
complete = False
while complete == False:
    try:
        bill = float(input("How much was the bill? "))
        if bill < 0:
            print("Bill amount should be positive.")
            continue
        tip = int(input("How much percent you want to tip? "))
        if tip < 0 or tip > 100:
            print("Tip percentage should be between 0 and 100.")
            continue
        people = int(input("How many people wants to split the bill? "))
        if people < 1:
            print("Number of people should be at least 1.")
            continue
        complete = True
    except ValueError:
        print("Please insert a valid number.")
    except ZeroDivisionError:
        print("Number of people should be more than 0.")

p_tip = 1 + tip/100 #% tip
p_bill = bill * p_tip #total with tip
total = p_bill / people #total per person

#Format the result to 2 decimal places
final_total = round(total, 2)
print(f"Each person should pay: £{final_total}")
