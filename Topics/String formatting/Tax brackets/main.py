income = float(input())

if income <= 15527:
    percent = 0
    calculated_tax = 0
elif income <= 42707:
    percent = 15
    calculated_tax = int(income * percent * 0.01)
elif income <= 132406:
    percent = 25
    calculated_tax = round(income * percent * 0.01)
else:
    percent = 28
    calculated_tax = round(income * percent * 0.01)

print(f"The tax for {int(income)} is {percent}%. That is {calculated_tax} dollars!")
