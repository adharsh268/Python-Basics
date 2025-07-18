#Write a Python program to find the sum of all elements in a list.

# numbers=[2,1,5,6,8]

# sum=0
# for x in numbers:
#     sum += x
# print(sum)

# #using range()
# sum1=0
# for y in range(0,len(numbers)):
#     sum1 += numbers[y]
# print(sum1)

# #using sum() function
# sum=sum(numbers)
# print(sum)

# print("-----------------------------------")


#Find the intersection and union of two lists.

# num1=[1,2,3,4,5,6,7,8]
# num2=[5,6,7,8,9,10,11,12]
# num11=set(num1)            #converting to sets
# num22=set(num2)

# num3=num11 & num22         #using intersection of sets

# # print(list(num3))          #converted back to list

# #using for loop
# for val in num1:
#     if val in num2:
#         print(val)


#list comprehension
# res=[val for val in num1 if val in num2]
# print(res)


# print("-----------------------------------")


#Convert a list to a tuple and vice versa.

# list1=['abc',2,4,'def']
# tup1=tuple(list1)
# print(tup1)

# list2=list(tup1)
# print(list2)


# print("-----------------------------------")


#Count occurrences of an element in a tuple.

# tup2=('abc','def',1,2,'abc',3,2,'abc',5,'abc',2)
# lis2=list(tup2)
# print(lis2.count('abc'))
# print(lis2.count(2))


# print("-----------------------------------")


# # Find the union, intersection, difference of two sets.

# set1={2,4,6,8,10}
# set2={1,2,3,4,5,6}

# print('union = ',set1.union(set2))
# print('union = ',set1|set2)


# print('intersection = ',set1.intersection(set2))
# print('intersection = ',set1 & set2)

# print('difference = ',set1.difference(set2))
# print('difference = ',set1-set2)

# print('difference2 = ',set2.difference(set1))



# print("-----------------------------------")


# Check if two sets are disjoint.

# set1={2,4,6,8,10}
# set2={1,2,3,4,5,6}
# set3={11,12,13,14}

# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))


# print("-----------------------------------")



# # Add and remove elements from a set.

# set2={1,2,3,4,5,6}

# set2.add(8)
# set2.add(10)
# print(set2)

# set2.remove(1)
# set2.remove(3)
# set2.remove(5)
# print(set2)



# print("-----------------------------------")


# Merge two dictionaries.
# dict1={'name':'adharsh', 'class':'btech'}
# dict2={'age':21, 'location':'alp'}

# dict1.update(dict2)
# print(dict1)



# print("-----------------------------------")



# # Create a list of n elements from user input.

# n=int(input("enter number of elements: "))
# list1=[]
# for x in range (n):
#     element=input(f'enter element {x+1} : ')
#     list1.append(element)
# print('list = ',list1)



# print("-----------------------------------")



# # Append, insert, and delete elements from a list.

# list1=['abc',2,4,'def',6,'ghi']

# list1.append(7)
# list1.append('jkl')
# print(list1)

# list1.insert(0,'hello')
# list1.insert(5,10)
# print(list1)

# del list1[3]
# print(list1)

# del list1[5]
# print(list1)



# print("-----------------------------------")



# Create a tuple with different data types.Access tuple elements by index. 
# Concatenate two tuples.
# Find the length of a tuple.
# Check if an element exists in a tuple.

# tup1= ('abc',1,2,3,'def',4,'ghi',12.5,'hello')

# x=tup1.index('def')
# y=tup1.index(12.5)
# print(x)
# print(y)


# tup2=('a',2,3,'d')
# tup3=(1,'b','c',4)
# tupf=tup2+tup3
# print(tupf)


# length=len(tup1)
# print(length)


# print('abc' in tup1)
# print(25 in tup1)
# print('world' in tup1)



# print("-----------------------------------")



# Create a dictionary with at least 5 key-value pairs.Access and print a value using its key.
# Update the value of an existing key.Add a new key-value pair to a dictionary.
# Delete a key from a dictionary using del or .pop().

# dict1={
#     'name':'nandhu',
#     'age':21,
#     'college':'stc',
#     'degree':'btech',
#     'year':3,
#     'loc':'cngr'
# }

# x=dict1['college']                     #accessing
# print(x)
# y=dict1['loc']
# print(y)


# dict1['loc']='chenagnnur'               #updating
# print(dict1)

# dict1['state']='kerala'                 #adding
# print(dict1)


# del dict1['loc']
# print(dict1)

# dict1.pop('degree')
# print(dict1)

# dict1.popitem()
# print(dict1)




# print("-----------------------------------")



# Create a set of integers from user input.
# Add a single element to a set.Add multiple elements to a set using .update().
# Remove an element using .remove() and .discard() — show the difference.
# Clear all elements from a set.


# n=int(input("enter number of elements: "))
# list1=[]
# for x in range (n):
#     element=int(input(f'enter element {x+1} : '))
#     list1.append(element)
# set1=set(list1)
# print(set1)


# set1={2,4,6,8}
# set1.add(3)
# print(set1)

# set2={'abc','def',5,9}
# set1.update(set2)
# print(set1)

# set1.remove(6)
# print(set1)
# # set1.remove(21)                  #remove() results error as the element is not present
# # print(set1)

# set1.discard('abc')
# print(set1)
# set1.discard('ac')                 #discard() does not return anything
# print(set1)

# set3={'abc','def',5,9,'sda',3,2,1}
# print(set3)
# set3.clear()                      #returns empty set
# print(set3)




# print("--------------------------------")



# # Find the symmetric difference between two sets.

# set1={2,3,4,5,'abc'}
# set2={3,4,5,'def'}
# x=set1.symmetric_difference(set2)
# print(x)



# print("-----------------------------------")



# #Remove common elements from a set.

# set11={1,'abc',2,3,'abc',2,1,'def'}
# print(set11)