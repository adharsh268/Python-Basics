#lists are mutable

# lst1=['a','b','c',1,2,3]
# print(type(lst1))                #type of data

# print(len(lst1))                 #length of list


#-----------------------accessing lists
# print(lst1[2])
# print(lst1[2:5])
# print(lst1[:5])
# print(lst1[:])
# print(lst1[3:])

#-----------------------changing values
# lst1[2]='cee'
# print(lst1)

# lst1[2:4]=['ce','de']
# print(lst1)

#----------------------insert-------------
# lst1.insert(3,'d')
# print(lst1)

# lst1.insert('e')              #error--position has to be mentioned
# print(lst1)




# lst2=[2,3,4,'d','e','f']
# #------------------append----------------add at the end of the list
# lst2.append(5)
# print(lst2)


#-----------extend---------------merging
# list3=['a','b','c']
# list4=['d','e','f']

# list3.extend(list4)
# print(list3)
# print(list4)

# list4.extend(list3)
# print(list4)

# list4.extend(list4)
# print(list4)

#-----------------remove------------------remove the (only one)mentioned value
# list3.remove('b')
# print(list3)


#----------------pop------------------specify index position
# list4.pop(2)
# print(list4)

# list3.pop()         #default--pop the last value
# print(list3)


# list1=['a','b','c','d','e','f']

# #---------------del------------------delete the elements/whole list
# del list1[2]
# print(list1)

# del list1              #will show error as list will be deleted
# print(list1)


#---------------------clear-----------------elements of the list will be cleared, the list will be there
# list1.clear()
# print(list1)       #empty list will be the output









# -----------------------------list comprehension---------------------------------to make the code more efficient

# #---------normal code
# list1=['apple','banana','kiwi']
# list2=[]

# for x in list1:
#     if 'a' in x:
#         list2.append(x)
# print(list2)



# #---------after comprehension
# list1=['apple','banana','kiwi']
# list2=[x for x in list1 if 'a' in x]
# print(list2)





# #--------------------sort----------------------
# list1=['d','s','a','w','c']
# list1.sort()    #alphabetically ascending order
# print(list1)

# list1.sort(reverse=True )    #alphabetically descending order
# print(list1)



# #--------------------copy-------------------------
# list1=['p','q','r',1,2,3]
# list2=list1.copy()
# print(list1)
# print(list2)




#--------------------join---------------------------
# list1=['a','b','c',1,2,3]
# list2=['d','e','f',4,5,6]

# # list3=list2+list1         #joins both lists
# # print(list3)

# # for x in list2:           #joins list2 into list1
# #     list1.append(x)
# # print(list1)




#----------------count-------------------
# list1=[1,3,5,2,3,1,2,3,5,6,3,1,1,2,3]
# # x=list1.count(3)
# # print(x)



#------------------index----------------------------
# list1=['apple','banana','cherry','kiwi','mango']
# print(list1.index('cherry'))
# print(list1.index('kiwi'))