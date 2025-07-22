# a built-in function used in iterables(list/tuple/set/....)
# only one expression is allowed in this function
# syntax:
#        lamda arguments:expression
#-------------------------------------------------------------------------------




# a=lambda x,y:x*y
# print(a(5,3))



# def myfun(n):
#     return lambda a:a*n          #lambda-built-in function
# result=myfun(2)               #value of 'n'
# print(result(11))             #value of 'a'

#--------------------------------------------------------------------------------

#types of anonymous functions:

#----------------------------------------------
#                     map()                     #applies a specified function to each item in an iterable and returns a map object.
#----------------------------------------------

# n=[1,2,3,4]
# def square(number):
#     return number*number
# square_no=map(square,n)
# print(square_no)                            # a map object for the result is obtained---
#                                             # we cannot see the result directly, 
#                                             # for that we have to convert it into list/tuple or any other iterable
# result=list(square_no)
# print(result)



#----------------------------------------------
#                     filter()                     #used to select specific elements from an iterable based on a given condition. 
#----------------------------------------------

# def checkEven(nums):
#     if nums%2==0:
#         return True
#     return False
# numbers=[1,2,3,4,5,6,7,8,9,10]

# even_no=filter(checkEven,numbers)
# print(even_no)                                  #this will return a filter object, which cannot determine the exact value

# result=set(even_no)                             #here converted to set, we can convert into any iterable type
# print(result)                                   



#----------------------------------------------
#                     reduce()                     # takes a sequence of items and "reduces" them down to a single, cumulative value.
#----------------------------------------------
#here the 'functools' module is accessed to import reduce() function

# from functools import reduce                   #importing reduce() function
# def add(x,y):
#     return x+y

# a=[1,2,3,4,5] 
# result=reduce(add,a)                    
# print(result)                                 #it directly returns the output value

