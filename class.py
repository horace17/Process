class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('Initialized school member: {}'.format(self.name))


    def tell(self):
        print('Name: "{}" Age:"{}"'.format(self.name, self.age),end="")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized teacher:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks= marks
        print('Initialized marks: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr.Kamau',40,3000)
s = Student('John',35,2000)

members = [t,s]

for member in members:
    member.tell()
