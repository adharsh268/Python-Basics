
# Write a class Student with the attributes name and age. Create two objects from this class.

# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f'name:{self.name}, age:{self.age}')

# c1=Students('adharsh','21')
# c2=Students('godly','22')

# print('------------------------------------------')

# Write a class Book that takes title and author as constructor parameters and prints them 
# when an object is created.

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         print(f'title: {self.title}, author: {self.author}')

# b1=Book('book1','abc')
# b2=Book('book2','def')

# print('------------------------------------------')

# Create a class Student with:
#  • Attributes: name, roll_no
#  • Constructor to initialize attributes
#  • A method display() to print student details

# class Student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no

#     def display(self):
#         print(f"Name : {self.name}, Roll No. : {self.roll_no}")

# s1=Student('adharsh',15)
# s1.display()

# s2=Student('nandhu',25)
# s2.display()

# print('------------------------------------------')

#  Create a class Rectangle:
#  • Attributes: length, width
#  • Constructor to initialize them
#  • Method area() that returns the area of the rectangle

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         area=self.length*self.width
#         print(f'area = {area}cm^2')

# r1=Rectangle(11,7)
# r1.area()

# r2=Rectangle(21,5)
# r2.area()

# print('------------------------------------------')

#  Create a class BankAccount with:
#  • Attributes: owner, balance (default = 0)
#  • Methods:
#  • deposit(amount)
#  • withdraw(amount)
#  • display_balance()

# class BankAccount:
#     def __init__(self,name,acc_no,pin):
#         self.acc_name=name
#         self._acc_no=acc_no
#         self.__pin=pin
#         self.__bal=0.0
    
#     def verify_pin(self,entered_pin):
#         return entered_pin == self.__pin
    
#     def deposit(self,amount,entered_pin):
#         if self.verify_pin(entered_pin):
#             if amount>0:
#                 self.__bal+=amount
#                 print(f"amount deposited: {amount}")
#             else:
#                 print("enter valid amount")
#         else:
#             print("invalid pin")

#     def withdraw(self,amount,entered_pin):
#         if self.verify_pin(entered_pin):
#             if 0<amount<self.__bal:
#                 self.__bal-=amount
#                 print(f"amount withdrawn: {amount}")
#             else:
#                 print("invalid amount/insufficient balance")
#         else:
#             print("invalid pin")

#     def get_bal(self,entered_pin):
#         if self.verify_pin(entered_pin):
#             print(f"balance : {self.__bal}")
#         else:
#             print("invalid pin")

# o1=BankAccount('abc',101,286)
# o1.get_bal(286)
# o1.deposit(1000,286)
# o1.get_bal(286)

# o1.withdraw(256,286)
# o1.get_bal(286)

# print('------------------------------------------')

#  Create class Shape with:
#  • Protected attribute _sides
#  • Method to set number of sides
#  • Subclass Triangle that sets sides to 3 using inherited method

# class Shape:
#     def __init__(self,sides):
#         self._sides=sides
#     def show_sides(self):
#         print(f"this shape has {self._sides} sides!")
# class Triangle(Shape):
#     def __init__(self):
#         Shape.__init__(self,3)

# t=Triangle()
# t.show_sides()