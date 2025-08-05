#modules
#set of functions stored in a file
#built-in or customized modules


#-------customized module-----------
# #-----mymod.py---------
# def greeting(name):
#     print("hello"+name)

# #-----file2.py---------
# import mymod
# file2.greeting('bob')




#----------------built-in modules ---------------

#----------------(1)--math module------------------
#used for mathematical functions

# #sqrt
# import math
# print(math.sqrt(9))


# #trignometry
# import math
# print(math.sin(0))
# print(math.sin(math.pi))


# #radian    degre-> radian
# import math
# print(math.radians(180))


# #multiply
# import math
# seq=(2,5,8)
# print(math.prod(seq))


# #power
# import math
# print(math.pow(2,4))


# #log
# import math
# print(math.log(8))


# #permutation
# import math
# print(math.perm(6,3))


# #greatest common divisor
# import math
# print(math.gcd(6,9))




#----------------(2)--datetime module------------------

# import datetime


# #current date & time

# x=datetime.datetime.now()
# print(x)

# #or

# print(x.year)
# print(x.month)
# print(x.day)

# from time import strftime
# print(strftime("%A"))         #weekday -full
# print(strftime("%a"))         #weekday -short

# print(strftime("%D"))            #date

# print(strftime("%B"))            #month
# print(strftime("%m"))            #month number
# print(strftime("%Y"))            #year
# print(strftime("%y"))            #year -last 2 digit


# print(strftime("%H"))            #hour
# print(strftime("%M"))            #minute 
# print(strftime("%S"))            #second

# print(strftime("%Y-%B-%d"))


#----------manually entering date and time

# import datetime

# dt = datetime.datetime(2025,8,26,15,30)
# print(dt)





#----------------(3)--random module------------------
# import random

#seed()- initialize random number generator

# random.seed(4)    #once a random value to generated for the specified seed value, it will not change after that
# print(random.random())


#randrange() 
# print(random.randrange(5,9)) # 9 not included, may also return float value


#randint()
# print(random.randint(4,7)) #both 4 & 7 included, only integer value


#random()
# print(random.random()) #----between 0 and 1


#choice -----random choice
# mylist=[2,56,'a','gfd',3,9]
# print(random.choice(mylist))


#shuffle 
# mylist=[2,56,'a','gfd',3,9]
# random.shuffle(mylist)
# print(mylist)


#sample

# mylist=[2,56,'a','gfd',3,9]
# print(random.sample(mylist,k=2))    #k is the parameter indicating number of random choices from a sequence

 
#uniform
# print(random.uniform(20,60))        #floating point between 20 & 60, both included






#----------------(4)--calendar module------------------

#calendar month
# import calendar
# yy=2003
# mm=8
# print(calendar.month(yy,mm))



#to check leap year
# print(calendar.isleap(2024))
# print(calendar.isleap(2003))



# print(calendar.calendar(2025))