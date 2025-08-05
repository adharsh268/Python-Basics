# # Write a program to find the transpose of a matrix.
# matrix=[
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]
# transpose=[]
# for i in range(0,3):
#     rows=[]
#     for j in range(0,3):
#         rows.append(matrix[j][i])
#     transpose.append(rows)

# print("original matrix : ")
# for row in matrix:
#     print(row)

# print("transposed matrix : ")
# for row in transpose:
#     print(row)


# print("-----------------------------------")


# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.

# n = int(input("How many lines? "))
# lines = []

# for i in range(n):
#     line = input()
#     lines.append(line.upper())

# print("Capitalized Lines:")
# for line in lines:
#     print(line)


# print("-----------------------------------")


# # Write a program to implement all built-in methods of list.

# my_list = [10, 20, 30, 40]

# print("Original list:", my_list)
# print("-----------------------------------")
# # append()
# my_list.append(50)
# print("After append:", my_list)
# print("-----------------------------------")
# # extend()
# my_list.extend([60, 70])
# print("After extend:", my_list)
# print("-----------------------------------")
# # insert()
# my_list.insert(2, 25)
# print("After insert:", my_list)
# print("-----------------------------------")
# # remove() 
# my_list.remove(40)
# print("After remove:", my_list)
# print("-----------------------------------")
# # pop() 
# last_item = my_list.pop()
# print("After pop():", my_list)
# print("Popped item:", last_item)
# print("-----------------------------------")
# # index() 
# index = my_list.index(30)
# print("Index of 30:", index)
# print("-----------------------------------")
# # count() 
# count = my_list.count(10)
# print("Count of 10:", count)
# print("-----------------------------------")
# # sort() 
# my_list.sort()
# print("After sort():", my_list)
# print("-----------------------------------")
# # reverse() 
# my_list.reverse()
# print("After reverse():", my_list)
# print("-----------------------------------")
# # copy() 
# copied_list = my_list.copy()
# print("Copied list:", copied_list)
# print("-----------------------------------")
# # clear() 
# my_list.clear()
# print("After clear():", my_list)


# print("-----------------------------------")


# # Write a program to read dictionary values through keyboard and merge
# # two dictionaries.

# def read_dict(n):
#     d={}
#     for i in range(n):
#         key=input(f'enter key{i+1}: ')
#         value=input(f'value for {key}: ')
#         d[key]=value
#     return d

# n1=int(input('enter no. of items in dict1: '))
# dict1=read_dict(n1)

# n2=int(input('enter no. of items in dict2: '))
# dict2=read_dict(n2)

# merged_dict=dict1.copy()
# merged_dict.update(dict2)

# print("dictionary 1 : ",dict1)
# print("dictionary 2 : ",dict2)
# print("merged dictionary : ",merged_dict)



# print("-----------------------------------")



# # Write a program to demonstrate all built-in methods of dictionary.

# my_dict = {
#     "name": "Alice",
#     "age": 25,
#     "city": "Delhi"
# }

# print("Original Dictionary:", my_dict)
# print("-----------------------------------")
# # 1. get()
# print("name:", my_dict.get("name"))
# print("-----------------------------------")
# # 2. keys() 
# print("keys():", my_dict.keys())
# print("-----------------------------------")
# # 3. values() 
# print("values():", my_dict.values())
# print("-----------------------------------")
# # 4. items() 
# print("items():", my_dict.items())
# print("-----------------------------------")
# # 5. update() 
# my_dict.update({"country": "India"})
# print("After update :", my_dict)
# print("-----------------------------------")
# # 6. pop()
# removed = my_dict.pop("age")
# print("After pop :", my_dict)
# print("Popped value:", removed)
# print("-----------------------------------")
# # 7. popitem() 
# last_item = my_dict.popitem()
# print("After popitem():", my_dict)
# print("Last removed item:", last_item)
# print("-----------------------------------")
# # 8. copy()
# copy_dict = my_dict.copy()
# print("Copied dictionary:", copy_dict)
# print("-----------------------------------")
# # 10. clear()
# my_dict.clear()
# print("After clear():", my_dict)
# print("-----------------------------------")


# Write a program to find the sum of all the elements in a list.
# list1=[2,4,6,8,10]
# sum=0
# for i in list1:
#     sum+=i
# print(sum)


# print("-----------------------------------")


# With a given integral number n, write a program to generate a
#  dictionary that contains(i,i*i) such that i is an integral number between 1
#  and n. And then the program should print the dictionary.

# n=int(input("enter an integer: "))
# squares={i:i*i for i in range(1,n+1)}
# print("dictionary = ",squares)


# print("-----------------------------------")


# Write a program that accepts a sentence and calculate the
# number of letters & digits.

# sentence = input("Enter a sentence: ")

# letters = 0
# digits = 0

# for char in sentence:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)


# print("-----------------------------------")


#  Write a program to implement filter(), map() and reduce() .

# from functools import reduce

# nums = [1, 2, 3, 4, 5, 6]

# # filter(): Keep even numbers
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print("Even numbers (filter):", even_nums)

# # map(): Square each number
# squares = list(map(lambda x: x * x, nums))
# print("Squares (map):", squares)

# # reduce(): Multiply all numbers
# product = reduce(lambda x, y: x * y, nums)
# print("Product (reduce):", product)



# print("-----------------------------------")


# Write a program to implement List Comprehension .

# evens = [x for x in range(1, 21) if x % 2 == 0]
# print("Even numbers:", evens)


# print("-----------------------------------")


#  Write a program to implement Dictionary Comprehension .

# squares_dict = {x: x*x for x in range(1, 6)}
# print("Dictionary of squares:", squares_dict)


# print("-----------------------------------")


# Write a program to find the largest and smallest element
#  from a list.

# nums = [23, 11, 56, 78, 4, 99]

# print("List:", nums)
# print("Largest:", max(nums))
# print("Smallest:", min(nums))


# print("-----------------------------------")


#  Write a Python program to print the numbers of a specified
#  list after removing even numbers from it. 

# nums = [10, 15, 20, 25, 30, 35, 40]

# odd_nums = [x for x in nums if x % 2 != 0]

# print("Original List:", nums)
# print("After Removing Even Numbers:", odd_nums)


# print("-----------------------------------")


#  Write a Python program to generate and print a list of first
#  and last 5 elements where the values are square of numbers
#  between 1 and 30

# squares = [x*x for x in range(1, 31)]

# result = squares[:5] + squares[-5:]

# print("First and Last 5 Squares:", result)


# print("-----------------------------------")


#  Write a Python program to insert a given string at the
#  beginning of all items in a list. 

# items = ['apple', 'banana', 'cherry']
# prefix = "Fruit: "

# updated = [prefix + item for item in items]

# print("Updated List:", updated)


# print("-----------------------------------")


# Write a Python program to iterate over two lists
#  simultaneously.

# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]

# # both lists are of the same length
# length = min(len(names), len(marks))

# for i in range(length):
#     print(names[i], "scored", marks[i])


# print("-----------------------------------")


# Write a Python program to add a key to a dictionary.

# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3  
# print("Updated Dictionary:", my_dict)


# print("-----------------------------------")


# Write a Python script to concatenate following dictionaries
# to create a new one.

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# concatenated = {}
# concatenated.update(dic1)
# concatenated.update(dic2)
# concatenated.update(dic3)

# print("Concatenated Dictionary : ", concatenated)


# print("-----------------------------------")


# Write a Python program to iterate over dictionaries using
#  for loops.

# print("\n19. Iterating over dictionary:")
# sample_dict = {'a': 1, 'b': 2, 'c': 3}

# for key, value in sample_dict.items():
#     print(f"Key: {key}, Value: {value}")


# print("-----------------------------------")


# Write a Python program to sum all the items in a dictionary.

# sum_dict = {'a': 10, 'b': 20, 'c': 30}
# total = sum(sum_dict.values())
# print("Sum of all values:", total)


# print("-----------------------------------")


#  Create a dictionary to hold information about pets. Each key is an
#  animal's name, and each value is the kind of animal.Eg : {'Willie':'Dog'}
#  Put at least 3 key-value pairs in your dictionary.
#  Use a for loop to print out a series of statements such as "Willie is a
#  dog."

# pets = {'Willie': 'dog', 'Milo': 'cat', 'Nemo': 'fish'}
# print("\n Pet Statements:")
# for name, kind in pets.items():
#     print(f"{name} is a {kind}.")


# print("-----------------------------------")


#  Write a python function to create and return a new dictionary from the
#  given dictionary (subject: mark).
#  Create a new dictionary with subject having marks more than 50.
#  marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# def filter_marks(marks_dict): 
#     return {subject: mark for subject, mark in marks_dict.items() if mark > 50}

# marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}

# filtered_marks = filter_marks(marks)
# print("Subjects with marks > 50:", filtered_marks)


# print("-----------------------------------")


#  Write a python function which accepts a sentence and finds the
#  number of letters and digits in the sentence.
#  It should return a dictionary in which the key should be letter count and
#  value should be digit count. Ignore the spaces or any other special
#  character in the sentence.

# def count_letters_digits(sentence):
#     letters = sum(c.isalpha() for c in sentence)
#     digits = sum(c.isdigit() for c in sentence)
#     return {'letter_count': letters, 'digit_count': digits}

# sentence = "Hello 123, my age is 20!"
# counts = count_letters_digits(sentence)
# print("result_dict = ", counts)


# print("-----------------------------------")


#  Write a Python function which generates and returns a dictionary
#  where the keys are numbers between 1 and n (both inclusive) and the
#  values are square of keys

# def generate_squares(n):
#     return {x: x ** 2 for x in range(1, n + 1)}

# squares_dict = generate_squares(5)
# print("Squares Dictionary :", squares_dict)