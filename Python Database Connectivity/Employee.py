# Here we are going to create the employee class which holds the information about an employee
class Employee:
    def __init__(self,employee_id,name,age,department,designation,salary,email=None,phone=None,date_of_joining = None):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary
        self.email = email
        self.phone = phone
        self.date_of_joining = date_of_joining