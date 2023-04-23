class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@ourcompany.com'

emp_1 = Employee('Jace', 'Goat', 40000)
emp_2 = Employee('Jack', 'Rabbit', '65000')

print(emp_1.email)
print(emp_2.email)


