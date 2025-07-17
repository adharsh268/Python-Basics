#key value pair
#ordered
# #no duplicates are allowed

# dict1={'name':'Adharsh',
#        'degree':'btech',
#        'year':3,
#        'age':21,
#        'college':'STC',
#        'marks':85,
#        'age':22}                  #age is defined twice as a key, thus the last value is considered
# print(dict1)

# #----------accessing dictionaries--------------
# x=dict1['age']
# print(x)
# #or
# y=dict1.get('marks')
# print(y)

# #to get only keys
# print(dict1.keys())

# #to get only values
# print(dict1.values())

# #to get the key-value pairs
# print(dict1.items())

#------------updating/adding new key-value pair-----------
# dict1['year']=4
# dict1['place']='chengannur'
# print(dict1)

#or

# dict1.update({'name':'nandhu'})
# print(dict1)

#---------------removing--------------------
# #pop
# dict1.pop('year')              #only the keys can be removed/pop,the key-value pair is poped out:values can only be replaced
# print(dict1)

# #popitem
# dict1.popitem()                  #the last inserted item is poped
# print(dict1) 

# #delete or del
# del dict1['degree']             #specified key os deleted
# print(dict1)

# del dict1                       #dictionary is deleted
# print(dict1)

# #------------------looping------------------------
# for x in dict1:                        #only the keys are printed
#     print(x)

# for x in dict1.keys():                 #to print only keys
#     print(x)

# for x in dict1.values():               #to print only values
#     print(x)

# for x,y in dict1.items():              #both key-value is printed
#     print(x,y)



#-----------------------nested dictionary----------------
# students={
#     'stud1':{
#         'name':'abc',
#         'year':3
#         },
#     'stud2':{
#         'name':'def',
#         'year':2
#         },
#     'stud3':{
#         'name':'ghi',
#         'year':4
#         }
# }
# print(students)

# print(students['stud1'])
# print(students['stud1']['name'])