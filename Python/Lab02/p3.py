class Details:
    def __init__(self, Id, Name, Gender, Company, Department):
        self.Id = Id
        self.Name = Name
        self.Gender = Gender
        self.Company = Company
        self.Department = Department


class Employee(Details):
    def __init__(self):
        self.empDetails = []

    def setEmployee(self, Id, Name, Gender, Company, Department):
        empDetail = Details(Id, Name, Gender, Company, Department)
        self.empDetails.append(empDetail)

    def showEmployee(self):
        for empDetail in self.empDetails:
            print("Id       : ", empDetail.Id)
            print("Name     : ", empDetail.Name)
            print("Gender   : ", empDetail.Gender)
            print("Company  : ", empDetail.Company)
            print("Department: ", empDetail.Department)


Id = input("Enter your ID: ")
name = input("Enter your Name: ")
Gender = input("Enter your Gender: ")
Company = input("Enter your Company's Location: ")
Dept = input("Enter your Department Number: ")

emp = Employee()
emp.setEmployee(Id, name, Gender, Company, Dept)
emp.showEmployee()
