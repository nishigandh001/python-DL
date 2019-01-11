# Creating a class Employee -Parent Class
class Employee:
    # Creating a data member to count the number of Employees
    employee_count = 0
    emp_avg_sal = 0

    #Creating a constructor and assiging varible names to parameters
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #Employee.employee_count +=1

    #creating avg_salary method to return fixed salary of an employee
    def avg_sal(self):
        return self.salary

#Child class
class Full_time_employee(Employee):
    total_sal = 0
    # Creating a constructor and assiging varible names to parameters
    def __init__(self, name, family, salary, department ):

       super().__init__(name,family,salary,department)
       Full_time_employee.total_sal += self.salary

       Employee.employee_count += 1
       #print(Full_time_employee.total_sal)

    # creating full_time_employee_avg_sal method to return the salary of an full-time employee
    def avg_sal(self): #polymorphism
        #avg_sal = Employee.avg_salary(self) + self.extra_salary
        Employee.emp_avg_sal += Employee.avg_sal(self)
        print("employees average salary: " , Full_time_employee.total_sal / Employee.employee_count)




emp1_family = { "members":4, "insurance_covered": 20000}
emp2_family = { "members":2, "insurance_covered": 10000}
emp = Employee("Bob", emp1_family, 10000, "HR")

#creatng object for Full_time employee class and passing values into it
emp1 = Full_time_employee("Billy", emp1_family, 10000, "Tecnical")
emp2 = Full_time_employee("p", emp2_family, 17360, "Tecni")
emp2.avg_sal()


print("Total number of employees in an organization: ", Employee.employee_count)
print("employee1 family" ,emp1.family)
print("employee 2 family", emp2.family)