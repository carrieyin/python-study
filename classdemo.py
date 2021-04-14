# by y_dd
# 时间 2021/04/12
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


ea=Employee('tom', 6000)
ea.displayCount()
ea.displayEmployee()
na=getattr(ea, 'name')
print(na)
print('__doc__', ea.__doc__)
print('__dict', ea.__dict__)
print('module', ea.__module__)
print("basis", ea.__bases__)

