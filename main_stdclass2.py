from std_module_class2 import StudentManager

class StudentApp:
    def __init__(self):
        self.manager = StudentManager()

    def show_menu(self):
        print("\n=== منو ===")
        print("1. Add std")
        print("2. Search std")
        print("3. Display std")
        print("4. Delete std")
        print("5. Edit std")
        print("6. Exit")
        print("============")

    def add_student(self):
        print("\n افزودن دانشجوی جدید")
        name = input("نام دانشجو: ").strip()
        age = input("سن دانشجو: ").strip()
        field = input("رشته تحصیلی: ").strip()
        self.manager.add_student(name, age, field)
        print("دانشجو با موفقیت اضافه شد")

    def search_student(self):
        print("\n جستجوی دانشجو")
        name = input("نام دانشجو برای جستجو: ").strip()
        result = self.manager.search_student(name)
        if result:
            for s in result:
                print(s.to_display())
        else:
            print("دانشجویی با این نام پیدا نشد")

    def display_students(self):
        print("\n لیست دانشجوها")
        students = self.manager.list_students()
        if not students:
            print("لیست دانشجوها خالی است")
        else:
            for i, s in enumerate(students, start=1):
                print(f"{i}) {s.to_display()}")

    def delete_student(self):
        print("\n حذف دانشجو")
        name = input("نام دانشجویی که میخواهید حذف کنید: ").strip()
        if self.manager.delete_student(name):
            print("دانشجو حذف شد")
        else:
            print("دانشجویی با این نام پیدا نشد")

    def edit_student(self):
        print("\n--- ویرایش دانشجو ---")
        name = input("نام دانشجویی که میخواهید ویرایش کنید: ").strip()
        new_name = input("نام جدید (خالی برای بدون تغییر): ").strip()
        new_age = input("سن جدید (خالی برای بدون تغییر): ").strip()
        new_field = input("رشته جدید (خالی برای بدون تغییر): ").strip()
        if self.manager.edit_student(name, new_name, new_age, new_field):
            print("اطلاعات دانشجو ویرایش شد")
        else:
            print("دانشجویی با این نام پیدا نشد")

    def run(self):
        while True:
            self.show_menu()
            choice_str = input("لطفا شماره گزینه را وارد کنید: ").strip()

            if not choice_str.isdigit():
                print("لطفا فقط عدد صحیح وارد کنید")
                continue

            choice = int(choice_str)

            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.search_student()
            elif choice == 3:
                self.display_students()
            elif choice == 4:
                self.delete_student()
            elif choice == 5:
                self.edit_student()
            elif choice == 6:
                print("خروج از برنامه، موفق باشید")
                break
            else:
                print("لطفا یک عدد صحیح بین ۱ تا ۶ وارد کنید")

if __name__ == "__main__":
    app = StudentApp()
    app.run()