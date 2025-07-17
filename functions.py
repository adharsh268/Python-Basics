#def

#------------------calling a function--------------------
# def funct1():
#     print('abc')
    
# funct1()



# #-----------------arguments------------------
# def funct2(name):
#     print('name : ',name +' nair')

# funct2('akash')
# funct2('raju')



#addition using a function
# def addition(x,y):
#     sum=x+y
#     print('sum =',sum)

# addition(3,5)
# addition(4,2)



# #-----default arguments---------
# def addi(a=3,b=5):
#     sum=a+b
#     print(sum)

# addi(2,3)               #both arguments are passed
# addi(2)                 #default taken as the first argument
# addi(b=9)               #other arguments have to be specified
# addi()                  #default values are calculated





# #------keyword arguments---------
# def info(fname,lname):
#     print(fname)
#     print(lname)

# # info(fname='cartel')          #error---as the other arguments are not specified
# info(fname='cartel',lname='thomas')




#-------arbitrary argument---------or------variable length argument------------
# def multi(*numbers):                     # *numbers-----any number of arguments can be passed
#     result=1
#     for num in numbers:
#         result*=num
#     print('result =',result)

# multi(9,4)
# multi(4,3,9,6,3)