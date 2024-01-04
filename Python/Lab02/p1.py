class StudentRecordSystem:
    def __init__(self):
        self.students_list = []

    def add_student(self):
        name = input("Enter the name of the student: ")
        roll_number = input("Enter the roll number: ")
        marks = input("Enter marks: ")

        student_info = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks
        }

        self.students_list.append(student_info)

    def display_records(self):
        print("Student Records:")
        i = 1
        for student in self.students_list:
            print(f"{i}. {student['name']} : {student['marks']} :: {student['roll_number']}")
            i += 1

    def run(self):
        while True:
            self.add_student()
            add_another = input("Add another student? [y/n]: ").lower()
            if add_another != 'y':
                break

        self.display_records()


student_system = StudentRecordSystem()
student_system.run()
