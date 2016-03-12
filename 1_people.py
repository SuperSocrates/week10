# let's explore inheritance and polymorphism

class Person:

  def __init__(self, name, hometown):
    self.name = name
    self.hometown = hometown

  def introduce(self):
    print("Hi, I'm {0}. I'm from {1}.".format(self.name, self.hometown))

  def meet(self, another):
    self.introduce()
    another.introduce()

class Employee(Person):

    def department(self):
        return "Software Consulting"


me = Employee("Tom", "Evanston")
print(me.department())
friend = Employee("Jeff", "Skokie")

me.meet(friend)
# Hi, I'm <your name>.  I'm from <your hometown>.
# Hi, I'm Jeff.  I'm from Skokie.
