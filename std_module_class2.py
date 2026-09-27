FILE_NAME = "students.txt3"


class Student:
    def __init__(self, name, age, field):
        self.name = name
        self.age = age
        self.field = field

    def to_line(self):
        return f"{self.name},{self.age},{self.field}"

    @staticmethod
    def from_line(line):
        parts = line.split(",")
        if len(parts) == 3:
            return Student(parts[0], parts[1], parts[2])
        return None

    def to_display(self):
        return f"نام: {self.name} | سن: {self.age} | رشته: {self.field}"

    def update(self, new_name="", new_age="", new_field=""):
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_field:
            self.field = new_field


class StudentManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.students = []
        self.load_students()

    def load_students(self):
        self.students = []
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    student = Student.from_line(line)
                    if student:
                        self.students.append(student)
        except FileNotFoundError:
            pass

    def save_students(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(s.to_line() + "\n")

    def add_student(self, name, age, field):
        self.students.append(Student(name, age, field))
        self.save_students()

    def search_student(self, name):
        return [s for s in self.students if s.name == name]

    def delete_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                self.save_students()
                return True
        return False

    def edit_student(self, name, new_name="", new_age="", new_field=""):
        for s in self.students:
            if s.name == name:
                s.update(new_name, new_age, new_field)
                self.save_students()
                return True
        return False

    def list_students(self):
        return self.students