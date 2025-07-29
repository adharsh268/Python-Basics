# ---------------------------------
#            generator 
# ---------------------------------
# 'yield' keyword is used instead of 'return' to produce a value in a function

# When yield is encountered, the function's execution is paused, 
# and the yielded value is returned. The function's state is saved, 
# and it resumes from that point when the next value is requested.

# Values are computed and yielded only when they are needed, using next() function


# def square(num):
#     for i in range(1,num+1):
#         yield i*i            # in place of return, yield is used to produce a value
    
# squ=square(5)
# print(next(squ))             # only one iteration is performeed, and the state of the function is saved
# print(next(squ))             # no. of iterations to be printed = no. of next() statement
# print(next(squ))
# print(next(squ))
# print(next(squ))





# ---------------------------------
#            decorator 
# ---------------------------------
# functions that operates on other functions.
# There is a nested function inside the decorator. It wraps the original function ---- wrapper
# 


# def outer(funct):
#     def inner():
#         print("hello")
#         funct()
#         print("world")
#     return inner
#--------------------------------------------------------------------------------------------------------------------------
# # ----method 1----
# @outer                                        #decorator
# def ordinary():
#     print("------------decorated-----------")
# ordinary()
#---------------------------------------------------------------------------------------------------------------------------
# #----method 2----
# def ordinary():
#     print("------------decorated-----------")
# ordinary=outer(ordinary)
# ordinary()
#--------------------------------------------------------------------------------------------------------------------------

