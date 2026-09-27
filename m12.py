def calculator(num1,num2,operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("خطا: تقسیم بر صفر ممکن نیست!")
            return result
        result = num1 / num2
    else:
        print("عملیات نامعتبره!")

    return result


    
num1 = float(input("number1:"))
operator = input(" (+,-,*,/):")
num2 = float(input("number2:"))
result = calculator(num1,num2,operator)
print("ماشین‌حساب")
print("عملیات‌ها: + - * /")
print(f"[جواب]: {result}")