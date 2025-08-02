#--------------------------------------------  access modifiers  -------------------------------------------------------------

#-------------------------
#         public
#-------------------------
# accessible from anywhere
# no underscore _ as prefix
class Person:
    def __init__(self, name):
        self.name = name  # public attribute

p = Person("Alice")
print(p.name)             #accessible




#-------------------------
#         protected
#-------------------------
# accessed only within the class and its subclasses.
# One underscore _ prefix.
# its not truly inaccessible, but accessing from outside the class or subclass is dicouraged or not recommended.
class Person:
    def __init__(self, name):
        self._name = name  # protected attribute

class Student(Person):     # subclass of Person
    def display_name(self):
        print("Name:", self._name)

s = Student("Bob")
s.display_name()   # Accessible in subclass
print(s._name)     # Technically accessible, but discouraged




#-------------------------
#         protected
#-------------------------
# Only accessible within the class.
# Two underscores __ prefix.
class Person: 
    def __init__(self, name):
        self.__name = name  # private attribute

    def show_name(self):
        print("Name:", self.__name)

p = Person("Charlie")
p.show_name()        # Allowed
# print(p.__name)    # AttributeError
print(p._Person__name)  # Name mangling allows access (not recommended)


# ------------------------------------name mangling----------------------------------------------------

# When you define a variable with two underscores (e.g., __name), Python internally changes its name to:
#                       _ClassName__attributeName           ie. _Person__name
