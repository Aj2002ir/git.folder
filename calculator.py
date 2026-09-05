def calculator():
    print("ماشین‌حساب")
    print("عملیات‌ها: + - * /")
    
    num1 = float(input("عدد اول رو وارد کن:"))
    operator = input("عملیات رو وارد کن (+,-,*,/):")
    num2 = float(input("عدد دوم رو وارد کن:"))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("خطا: تقسیم بر صفر ممکن نیست!")
            return
        result = num1 / num2
    else:
        print("عملیات نامعتبره!")
        return
    
    print(f"نتیجه: {result}")

calculator()