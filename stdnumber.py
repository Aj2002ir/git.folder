
name = input("نام دانشجو: ")
student_id = input("شماره دانشجویی: ")
major = input("رشته تحصیلی: ")

n = int(input("تعداد درس‌های این ترم: "))

scores = []
units_sum = 0

for i in range(n):
    course_name = input(f"نام درس {i+1}: ")
    score = float(input(f"نمره درس {i+1}: "))
    units = int(input(f"تعداد واحد درس {i+1}: "))
    scores.append((course_name, score, units))
    units_sum += units

total_points = sum(score * units for _, score, units in scores)
average = total_points / units_sum

if average >= 12:
    status = "قبول (بدون مشروطی)"
else:
    status = "مشروط"
    
print("-" * 40)
print(f"نام: {name}")
print(f"شماره دانشجویی: {student_id}")
print(f"رشته: {major}")
print(f"مجموع واحدهای این ترم: {units_sum}")
print("نمرات دروس:")
for course_name, score, units in scores:
    print(f"  - {course_name}: نمره {score} | واحد {units}")
print(f"معدل کل: {average:.2f}")
print(f"وضعیت: {status}")
    