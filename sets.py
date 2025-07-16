#{ }
#unordered 
#no duplicateds are allowed

#-----------printing sets
# set1={'apple','banana','mango','apple'}
# print(set1)

# set2={True,1,0,'hello'}
# print(set2)

#-----------accessing sets------------ 
#using loop and membership operators

# set1={'apple','banana','mango'}
# # for x in set1:
# #     print(x)

# print('banana' in set1)

#-------------add items in sets-------------
# set1={'apple','banana','mango'}
# set1.add('orange')
# print(set1)


#-------------add sets-----------------
#merging -------- update()

# set1={'apple','banana','mango'}
# set2={'kiwi','cherry','berry'}
# set1.update(set2)
# print(set1)


#-----------adding list items in a set--------
# set1={'apple','banana','mango'}
# list1=['kiwi','cherry','berry']
# set1.update(list1)
# print(set1)


#-----------------remove-----------------  discard() can also be used to remove an item from sets
# set1={'berry', 'kiwi', 'apple', 'cherry', 'banana', 'mango'}
# set1.remove('banana')
# print(set1)
# set1.discard('mango')
# print(set1)



#----------------randomly remove items---------------using pop()
# set1={'berry', 'kiwi', 'banana', 'mango'}
# x=set1.pop()
# print(x)
# print(set1)


#---------------clear--------------
# set1={'berry', 'kiwi', 'banana', 'mango'}
# set1.clear()                                   #empty set
# print(set1)


#----------------delete--------------    #entirely delete the set
# set1={'berry', 'kiwi', 'banana', 'mango'}
# del set1
# print(set1)


#---------------------------------------------join operatios----------------------------------------------------
#----------union-----------

# set1={'apple','banana','mango'}
# set2={'kiwi','apple','berry'}
# set3=set1.union(set2)
# print(set3)
# #or
# set4=set1 | set2
# print(set4)

#----------intersection-----------
# set1={'apple','banana','mango'}
# set2={'kiwi','apple','berry'}
# set3=set1.intersection(set2)
# print(set3)
# #or
# set4=set1 & set2
# print(set4)


#-----------difference------------
# set1={'apple','banana','mango'}
# set2={'kiwi','apple','berry'}

# set3=set1.difference(set2)
# print(set3)
# set4=set2.difference(set1)
# print(set4)

#or

# set3=set1-set2
# print(set3)
# set4=set2-set1
# print(set4)



# #---------------symmetric difference----------------
# set1={'apple','banana','mango'}
# set2={'kiwi','apple','berry'}
# set3=set1.symmetric_difference(set2)
# print(set3)
# #or
# set4=set1^set2
# print(set4)



#------------------isdisjoint()-------------
# x={'apple','banana','mango'}
# y={'kiwi','apple','berry'}
# z=x.isdisjoint(y)
# print(z)

# a={1,2,3,4}
# b={5,6,7,8}
# c=a.isdisjoint(b)
# print(c)