#----------indexing and slicing-------------------- 
#  str1='ernakulam south'

# print(str1[2])
# print(str1[-4])
# print(str1[2:8])
# print(str1[-8:-1]) #last word is not printed
# print(str1[-8:0]) #no output---exception in python string

# str2='ernakulam south ' #--a space is added at the end
# print(str2[-9:-1])




#-----------modification functions--


#upper case and lower case

# txt='hElLo WorlD'
# print(txt.upper())
# print(txt.lower())



#strip
# a=' hello World   '
# print(a)
# print(a.strip())



#replace
# a='hello world'
# print(a.replace("l","o"))
# print(a.replace("hello","hai"))



#split
# a='hi hello world '
# b=a.split(" ")
# print(b)

# c='hi,hello world'
# d=c.split(",")
# print(d)



#count
# a='my eat apples everyday, apple is red in color'
# print(a.count('apple'))
# print(a.count('apples'))
# print(a.count(' '))



#startswith and endswith
# a='hi i eat apples everyday'
# c=a.startswith('hi')
# d=a.endswith('day')
# print(c)
# print(d)
# p=a.startswith('hello')
# q=a.endswith('every')
# print(p)
# print(q)



#isnumeric
# str1='hi hello '
# str2='3546789.9'
# str3='3546789'
# print(str1.isnumeric())
# print(str2.isnumeric())
# print(str3.isnumeric())



#--------------string concatenation-------------
# a='hello'
# b='world'
# c=a+b
# d=a+" "+b
# print(c)
# print(d)



#----------string format---------
# age=32
#txt='i am'+age+'years old'  #error
# print(txt)
#----------------f strings--------------
# txt1=f'i am {age} years old'
# print(txt1)


# price=59
# txt2=f'the price is {price:.2f} dollars'
# print(txt2)
