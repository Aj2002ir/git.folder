def main():
    name = input("نام دانشجو: ")
    major = input("رشته تحصیلی: ")
    n = int(input("تعداد درس‌های این ترم: "))

    total_points = 0

    print("نمرات دروس:")
    for i in range(n):
        course_name = input(f"نام درس {i+1}: ")
        score = float(input(f"نمره درس {i+1}: "))
        total_points += score 
        print(f"  - {course_name}: نمره {score}")

    average = total_points / n

    status = "قبول (بدون مشروطی)" if average >= 12 else " مشروط "
    
    print(f"نام: {name}")
    print(f"رشته: {major}")
    print(f"معدل کل: {average:.2f}")
    print(f"وضعیت: {status}")
main()
    