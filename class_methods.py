class Person:
     name = "anonymous"

     @classmethod
     def changeName(cls,name):
          cls.name = name

p1 = Person()
p1.changeName("Rahul kumar")
print(p1.name)
print(Person.name)

