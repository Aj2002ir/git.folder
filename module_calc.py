def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("خطا: تقسیم بر صفر ممکن نیست!")
            return None

        result = num1 / num2

    else:
        print("عملیات نامعتبره!")
        return None

    return result