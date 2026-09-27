from std_module_class import StudentManager

manager = StudentManager()

def show_menu():
    print("\n=== منو ===")
    print("1. Add std")
    print("2. Search std")
    print("3. Display std")
    print("4. Delete std")
    print("5. Edit std")
    print("6. Exit")

while True:
    show_menu()
    choice = input("لطفا شماره گزینه را وارد کنید: ").strip()

    if not choice.isdigit():
        print("لطفا فقط عدد وارد کنید")
        continue

    choice = int(choice)

    if choice == 1:
        name = input("نام: ").strip()
        age = input("سن: ").strip()
        field = input("رشته: ").strip()
        manager.add(name, age, field)
        print("اضافه شد")

    elif choice == 2:
        name = input("نام برای جستجو: ").strip()
        result = manager.search(name)
        if result:
            for s in result:
                print(f"نام: {s['name']} | سن: {s['age']} | رشته: {s['field']}")
        else:
            print("پیدا نشد")

    elif choice == 3:
        if not manager.students:
            print("لیست خالی است")
        else:
            for i, s in enumerate(manager.students, start=1):
                print(f"{i}) نام: {s['name']} | سن: {s['age']} | رشته: {s['field']}")

    elif choice == 4:
        name = input("نام برای حذف: ").strip()
        print("حذف شد" if manager.delete(name) else "پیدا نشد")

    elif choice == 5:
        name = input("نام برای ویرایش: ").strip()
        new_name = input("نام جدید (اختیاری): ").strip()
        new_age = input("سن جدید (اختیاری): ").strip()
        new_field = input("رشته جدید (اختیاری): ").strip()
        print("ویرایش شد" if manager.edit(name, new_name, new_age, new_field) else "پیدا نشد")

    elif choice == 6:
        print("خروج، موفق باشید")
        break
    
    else:
        print("عدد بین ۱ تا ۶ وارد کنید")