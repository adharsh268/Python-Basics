# tup1=('apple','banana','mango')

#---------------update tuples-----------
# tuples cannnot be directly updated,append, first it has to be converted into list, then update and then converted back to tuple

# tup1=('apple','banana','mango')
# y=list(tup1)
# y[1]='kiwi'
# tup1=tuple(y)
# print(tup1)

#------------add items-------------------
# tup1=('bmw','kia','maruti')
# y=list(tup1)
# y.append('benz')
# tup1=tuple(y)
# print(tup1)

#------------adding tuples----------------
# tup1=('a','b','c','d')
# tup2=('e',)                   #comma is used to indicate that this is a tuple, otherwise is considered a string
# tup1 += tup2
# print(tup1)

#------------remove-------------------
# tup1=('bmw','kia','maruti')
# y=list(tup1)
# y.remove('bmw')
# tup1=tuple(y)
# print(tup1)

#------------delete-----------------
# tup1=('bmw','kia','maruti')

# del tup1[1]           #cannot be directly deleted
# print(tup1)

# del tup1              #whole tuple can be deleted using del
# print(tup1)

#--------------join----------------
# tup1=('a','b','c')
# tup2=('d','e','f')
# tup3= tup1+tup2
# print(tup3)

# #---------------multiplication-------------
# tup1=('abc','def','ghi')
# mytup=tup1*3
# print(mytup)

#------------------count---------------------
# tup1=(1,2,3,4,3,4,2,2,4,3,2)
# x=tup1.count(2)
# print(x)

#-----------------index--------------------
# tup1=(1,2,3,4,3,4,2,5,2,4,3,2)
# x=tup1.index(5)
# print(x)