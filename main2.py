import module_cal1

print("--- Simple Calculator ---")

try:
    num1 = float(input("Enter the first number: "))
    op = input("Operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == '+':
        res = module_cal1.add(num1, num2)
    elif op == '-':
        res = module_cal1.subtract(num1, num2)
    elif op == '*':
        res = module_cal1.multiply(num1, num2)
    elif op == '/':
        res = module_cal1.divide(num1, num2)
    else:
        res = "Invalid operator! Only +, -, *, / are allowed!"

    print(f"\nResult: {res}\n")

    with open("riazy.txt", "a") as file:
        file.write(f"{num1} {op} {num2} = {res}\n")

except ValueError:
    print("Error: Please enter a valid number!")