# ------ حالت w (نوشتن اطلاعات دانشجوها) ------
# اگه فایل موجود نباشه ایجاد میشه، اگه باشه محتوای قبلی پاک میشه

students = []
n = int(input("چند دانشجو می‌خوای وارد کنی؟ "))

for i in range(n):
    print(f"\nدانشجوی شماره {i+1}:")
    student_id = input("کد دانشجویی: ")
    name = input("اسم: ")
    age = input("سن: ")
    students.append((student_id, name, age))

with open("students.txt", "w", encoding="utf-8") as f:
    for student_id, name, age in students:
        f.write(f"{student_id},{name},{age}\n")

print("\nحالت w: اطلاعات دانشجوها در students.txt ذخیره شد.")


# ------ حالت r (خواندن اطلاعات دانشجوها) ------
with open("students.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("\nحالت r: محتوای فایل students.txt:")
print(content)


# ------ حالت a (اضافه کردن دانشجوی جدید) ------
with open("students.txt", "a", encoding="utf-8") as f:
    print("\nاضافه کردن یک دانشجوی جدید:")
    student_id = input("کد دانشجویی: ")
    name = input("اسم: ")
    age = input("سن: ")
    f.write(f"{student_id},{name},{age}\n")

print("\nحالت a: دانشجوی جدید به انتهای فایل اضافه شد.")

with open("students.txt", "r", encoding="utf-8") as f:
    print("\nمحتوای فایل بعد از اضافه شدن:")
    print(f.read())


# ------ حالت x (ساخت فایل پشتیبان جدید) ------
# اگه فایل موجود نباشه ایجاد میشه، اگه باشه خطا میده
try:
    with open("students_backup.txt", "x", encoding="utf-8") as f:
        with open("students.txt", "r", encoding="utf-8") as source:
            f.write(source.read())
    print("\nحالت x: فایل پشتیبان students_backup.txt ساخته شد.")
except FileExistsError:
    print("\nحالت x: خطا! فایل students_backup.txt از قبل وجود داره.")