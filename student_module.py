FILE_NAME = "students.txt"
def load_students():
    students = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    students.append({"name": parts[0],"age": parts[1],"field": parts[2]})
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s['name']},{s['age']},{s['field']}\n")

def add_student(students, name, age, field):
    students.append({"name": name, "age": age, "field": field})
    save_students(students)
def search_student(students, name):
    return [s for s in students if s["name"] == name]

def delete_student(students, name):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            save_students(students)
            return True
    return False

def edit_student(students, name, new_name="", new_age="", new_field=""):
    for s in students:
        if s["name"] == name:
            if new_name:
                s["name"] = new_name
            if new_age:
                s["age"] = new_age
            if new_field:
                s["field"] = new_field
            save_students(students)
            return True
    return