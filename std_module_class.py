FILE_NAME = "students.txt1"


class StudentManager:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.students.append({"name": parts[0], "age": parts[1], "field": parts[2]})
        except FileNotFoundError:
            pass

    def save(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s['name']},{s['age']},{s['field']}\n")

    def add(self, name, age, field):
        self.students.append({"name": name, "age": age, "field": field})
        self.save()

    def search(self, name):
        return [s for s in self.students if s["name"] == name]

    def delete(self, name):
        for s in self.students:
            if s["name"] == name:
                self.students.remove(s)
                self.save()
                return True
        return False

    def edit(self, name, new_name="", new_age="", new_field=""):
        for s in self.students:
            if s["name"] == name:
                if new_name:
                    s["name"] = new_name
                if new_age:
                    s["age"] = new_age
                if new_field:
                    s["field"] = new_field
                self.save()
                return True
        return False