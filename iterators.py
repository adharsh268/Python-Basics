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
class MyNum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        # x=self.a
        self.a+=1
        return self.a

MyClass=MyNum()
myiter=iter(MyClass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


