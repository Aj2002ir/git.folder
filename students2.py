
n = int(input("چند دانشجو می‌خوای وارد کنی؟ "))
file =open("student.tex","a")
for i in range(n):
    print(f"\nدانشجوی شماره {i+1}:")
    student_id = input("کد دانشجویی: ")
    name = input("اسم: ")
    age = input("سن: ")
    file.write(name:("اسم"\n))
    file.write(ege: ("سن"\n))                 
    file.write(numbers:("کد دانشجویی"\n))
    file.write()                                