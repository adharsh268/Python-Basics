# ------------------------------
#         iterators
# ------------------------------




# mytuple=('apple','banana','cherry')
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))


# mystr='banana'
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# ------use of iterators in a class---------
# class MyNum:
#     def __iter__(self):             # return the iterator object itself.
#         self.a=1
#         return self
#     def __next__(self):             # returning the next element from the iterator.
#         x=self.a
#         self.a+=1
#         return x

# MyClass=MyNum()
# myiter=iter(MyClass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))






# @staticmethod
# the @staticmethod decorator is used to define a method within a class that belongs to the class itself, 
# rather than to an instance of the class. 
# Unlike regular instance methods, static methods don't implicitly receive the self parameter
# as their first argument.
# operate independently - no instances are required

# class MyClass:
#     @staticmethod
#     def greet (name):
#         return f'hello {name}'
    
# print(MyClass.greet('alice'))





# @classmethod - take cls as its first argument
# used to define a method within a class that operates on the class itself 
# rather than a specific instance of the class.

class myClass:
    count=0     # class variable
    def __init__(self,name):
        self.name=name
        myClass.count+=1
        
    @classmethod
    def get_count(cls):
            return cls.count
        
obj1=myClass('alice')
obj2=myClass('bobo')

print(myClass.get_count())