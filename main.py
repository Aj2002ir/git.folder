"""
فایل اصلی برنامه مدیریت دانشجویان
منو را نمایش می‌دهد و توابع را از student_module وارد می‌کند
"""

import student_module


def show_menu():
    print("\n========= منو =========")
    print("1. Add std")
    print("2. Search std")
    print("3. Display std")
    print("4. Delete std")
    print("5. Edit std")
    print("6. Exit")
    print("========================")


def main():
    students = student_module.load_students()

    while True:
        show_menu()
        choice_str = input("لطفا شماره گزینه را وارد کنید: ").strip()

        if not choice_str.isdigit():
            print("⚠️ لطفا فقط عدد صحیح وارد کنید.")
            continue

        choice = int(choice_str)

        if choice == 1:
            print("\n--- افزودن دانشجوی جدید ---")
            name = input("نام دانشجو: ").strip()
            age = input("سن دانشجو: ").strip()
            field = input("رشته تحصیلی: ").strip()
            student_module.add_student(students, name, age, field)
            print("✅ دانشجو با موفقیت اضافه شد.")

        elif choice == 2:
            print("\n--- جستجوی دانشجو ---")
            name = input("نام دانشجو برای جستجو: ").strip()
            result = student_module.search_student(students, name)
            if result:
                for s in result:
                    print(f"نام: {s['name']} | سن: {s['age']} | رشته: {s['field']}")
            else:
                print("❌ دانشجویی با این نام پیدا نشد.")

        elif choice == 3:
            print("\n--- لیست دانشجوها ---")
            if not students:
                print("لیست دانشجوها خالی است.")
            else:
                for i, s in enumerate(students, start=1):
                    print(f"{i}) نام: {s['name']} | سن: {s['age']} | رشته: {s['field']}")

        elif choice == 4:
            print("\n--- حذف دانشجو ---")
            name = input("نام دانشجویی که می‌خواهید حذف کنید: ").strip()
            if student_module.delete_student(students, name):
                print("✅ دانشجو حذف شد.")
            else:
                print("❌ دانشجویی با این نام پیدا نشد.")

        elif choice == 5:
            print("\n--- ویرایش دانشجو ---")
            name = input("نام دانشجویی که می‌خواهید ویرایش کنید: ").strip()
            new_name = input("نام جدید (خالی برای بدون تغییر): ").strip()
            new_age = input("سن جدید (خالی برای بدون تغییر): ").strip()
            new_field = input("رشته جدید (خالی برای بدون تغییر): ").strip()
            if student_module.edit_student(students, name, new_name, new_age, new_field):
                print("✅ اطلاعات دانشجو ویرایش شد.")
            else:
                print("❌ دانشجویی با این نام پیدا نشد.")

        elif choice == 6:
            print("خروج از برنامه. موفق باشید 👋")
            break

        else:
            print("⚠️ لطفا یک عدد صحیح بین 1 تا 6 وارد کنید.")


if name == "main":
    main()