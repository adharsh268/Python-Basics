#--------------OOPS--------------------------
# bottom-up approach - starts by creating small instances(objects) and then integrate them to a single program



#---------------------------------------
#             Class
#---------------------------------------

# Class'es are blueprints for creating objects. 
# A class defines a set of attributes and methods that the created objects (instances) can have.

#---------------------------------------
#             Object
#---------------------------------------

# An object is a specific instance of a class. 
# It holds its own set of data (instance variables) and can invoke the methods defined by its class. 
# Multiple objects can be created from the same class, each with its own unique attributes.


# class Person:
#     age=22
# print(Person)          #trying to print class directly--will not provide any output
# p1=Person()            #creating object
# print(p1.age)          #trying to access the class using a object
#----------it is the basic method to create a class object,commonly not used.-----------


#--------------------constructor-----------------------
# is a special method used to initialize objects when they are created from a class.
# is defined by the __init__ method.
# self within the __init__ method refers to the instance of the class that is being created.

# class Student:
#     def __init__(self, name, age):      #constructor
#         self.name=name                  #s1.name=name
#         self.age=age                    #s1.age=age
#     def display(self):
#         print(f"Name : {self.name}, Age : {self.age}")

# s1=Student('Adharsh',21)            #creating a object s1 for class Student
# s1.display()                        #accessing the method in a class



#--------------------------------------
            # Access Modifiers
#--------------------------------------

#Public
# no underscore
# it can be accessed from any point of the program

# class Person:
#     def __init__(self,name):
#         self.name=name            #public
# p=Person('Adharsh')
# print(p.name)



#protected
# single underscore
# it is accessed inside a class or by a subclass
#it can be accessed by other class but is not recommended

# class Employee:
#     def __init__(self):
#         self._salary=50000                 #protected
# class outsider:
#     def salary(self,emp):
#         print(emp._salary)
    
# e=Employee()
# o=outsider()
# print(e._salary)                           #correct way
# o.salary(e)                                #technically possible but not recommended



#private
# double underscore
# it is accessed inside a class only

# class Person:
#     def __init__(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
    
# p=Person('charles')
# print(p.get_name())                      #correct way
# # print(p.__name)                        #error
# print(p._Person__name)                   #not recommended