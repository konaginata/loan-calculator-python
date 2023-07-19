a = float(input())
b = float(input())
operator = input()


def divisions():
    if b == 0:
        print("Division by 0!")
    elif operator == "/":
        print(a / b)
    elif operator == "mod":
        print(a % b)
    else:
        print(a // b)


if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "pow":
    print(a ** b)
else:
    divisions()
