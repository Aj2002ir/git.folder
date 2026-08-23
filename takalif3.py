name = input(" نام ")
family = input(" نام خانوادگی  ")
age = int(input(" سن "))
grade = float(input(" نمره "))
print("نام و نام خانوادگی:", name, family)
print("سن:", age)
print("نمره:", grade)
if grade >= 18:
    print("وضعیت الف")
elif grade >= 13:
    print("وضعیت قابل قبول")
elif grade >= 10:
    print("وضعیت نیاز به تلاش بیشتر")
else:
    print("وضعیت رد")
    