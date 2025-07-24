# Square a number using a lambda function

square=lambda x:x*x
n=int(input("enter the number : "))
print(square(n))


print("---------------------------------------")


# Add two numbers using lambda

add=lambda x,y:x+y
a=int(input("enter 1st number : "))
b=int(input("enter 2nd number : "))
print(add(a,b))



print("---------------------------------------")


# Use lambda and map() to square all numbers in a list

n=[1,3,5,7,9]
square=lambda n:n*n                 #function
square_no=map(square,n)             #map()
print(square_no)
result=list(square_no)              #converting to list
print(result)


print("---------------------------------------")


# Use lambda and filter() to get even numbers

n=[2,3,5,6,8,9,21,56]
even=lambda n:n%2==0                 #condition
even_no=filter(even,n)               #filter()
print(even_no)
result=tuple(even_no)                #converting to tuple
print(result)


print("---------------------------------------")


# Sort a list of tuples based on the second value using lambda

a = [(5, 4), (1, 2), (3, 6), (2,1)] 
a.sort(key=lambda x: x[1])
print(a)


print("---------------------------------------")


# Use lambda with reduce() to compute the product of all elements

from functools import reduce                   #importing reduce() function
mul=lambda x,y:x*y

a=[1,2,3,4,5] 
result=reduce(mul,a)                    
print(result)                                 


print("---------------------------------------")


# Use lambda with map() to convert a list of strings to uppercase ::  words = ['hello', 'world']

words = ['hello', 'world']
upper=lambda x:x.upper()
upper_case=map(upper,words)
print(upper_case)
result=list(upper_case)
print(result)


print("---------------------------------------")


# Sort a list of dictionaries by a key using a lambda
people = [
{"name": "Alice", "age": 30},
{"name": "Bob", "age": 25},
{"name": "Charlie", "age": 35}
]

people.sort(key=lambda x: x['age'])
print(people)


print("---------------------------------------")


# Write a function that returns a lambda that multiplies by a given number

def function1(x):
    return lambda y:x*y

result=function1(3)
print(result(11))


print("---------------------------------------")


# Use lambda to sort a list of strings by the number of vowels

words = ['apple', 'banana', 'grape', 'kiwi']
words.sort(key=lambda words: sum(ch in 'aeiou' for ch in words),reverse=True)
print(words)


print("---------------------------------------")


# Use lambda and filter() to get palindromes from a list
words = ['madam', 'hello', 'noon', 'python']

key=lambda str1:str1==str1[::-1]
palindrome=filter(key,words)
print(palindrome)
result=list(palindrome)
print(result)


print("---------------------------------------")


# Use lambda with reduce() to concatenate only capitalized strings
words = ['Hello', 'world', 'From', 'python']

from functools import reduce
key = reduce(lambda acc, s: acc + s if s[0].isupper() else acc, words)

print(key)


print("---------------------------------------")


# Filter products by price range using filter() and lambda
products = [
{"name": "Laptop", "price": 900},
{"name": "Phone", "price": 500},
{"name": "Tablet", "price": 300},
{"name": "Monitor", "price": 200}
]

key=lambda product: 300 <= product["price"] <= 800
filtered_products = filter(key, products)

print(list(filtered_products))


print("---------------------------------------")


# Categorize numbers into even or odd using map() and lambda

numbers = [10, 15, 22, 33, 42]

key=lambda x:(x,"even" if x%2==0 else "odd")
result=map(key,numbers)
print(list(result))


print("---------------------------------------")


# Use lambda to extract domain names from emails

emails = ['alice@example.com', 'bob@gmail.com', 'carol@yahoo.com']
key = lambda email: email.split('@')[1]
result = map(key,emails)
print(list(result))