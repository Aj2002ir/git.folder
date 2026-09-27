import madol_cd

print("--- Simple Calculator ---")

try:
    num1 = float(input("Enter the first number: "))
    op = input("Operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == '+':
        res = madol_cd.add(num1, num2)
    elif op == '-':
        res = madol_cd.subtract(num1, num2)
    elif op == '*':
        res = madol_cd.multiply(num1, num2)
    elif op == '/':
        if num2 == 0:
           res = madol_cd.divide(num1,num2)
    else:       
        print("Invalid operator! Only +, -, *, / are allowed!")
    print(f"\n result: {res}\n")
    file = open("riazi.text","a")
    file.write(f"{num1}{op}{num2}={res}\n")
    (file.close)
except ValueError:
    print("Error: Please enter a valid number!")