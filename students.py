import sqlite3

# اتصال به دیتابیس (فایل students.db ساخته میشه اگه نباشه)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# ساخت جدول (فقط بار اول ساخته میشه)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    name TEXT,
    age INTEGER
)
""")

n = int(input("چند دانشجو می‌خوای وارد کنی؟ "))

for i in range(n):
    print(f"\nدانشجوی شماره {i+1}:")
    student_id = input("کد دانشجویی: ")
    name = input("اسم: ")
    age = input("سن: ")

    cursor.execute(
        "INSERT INTO students (student_id, name, age) VALUES (?, ?, ?)",
        (student_id, name, age)
    )

conn.commit()
conn.close()

print("\ ذخیره شد.")