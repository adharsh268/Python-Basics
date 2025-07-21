# Write a function that returns the square of a number.

def square(num):
    res=num*num
    print("square = ",res)

num=int(input("enter the number : "))
square(num)



print("--------------------------------------")



# Write a function that checks if a number is even or odd.
def check(num):
    if num%2==0:
        print("even number")
    else:
        print("odd number")

num=int(input("enter the number = "))
check(num)



print("--------------------------------------")



# Write a function that adds two numbers.

def add2num(num1,num2):
    sum=num1+num2
    print("sum = ",sum)

num1=int(input("enter 1st number = "))
num2=int(input("enter 2nd number = "))
add2num(num1,num2)



print("--------------------------------------")



# Write a function that returns the factorial of a number.

def fact(num):
    res=1
    for i in range(1,num+1):
        res*=i
    print("factorial = ",res)

num=int(input("enter the number = "))
fact(num)



print("--------------------------------------")



# Write a function to check if a string is a palindrome.

def palindrome(str1):
    rev_str=str1[::-1]
    if str1==rev_str:
        print("palindrome")
    else:
        print("not palindrome")

str1=input("enter the string : ")
palindrome(str1)



print("--------------------------------------")



# Write a function to find the maximum number in a list.

def maxlist1(numbers):
    res=max(numbers)
    print(res)

maxlist1([2,4,6,23,14])
maxlist1([3,8,9,24,89])

#or 

def maxlist2(numbers):
    maxi=numbers[0]
    for i in range(1,len(numbers)):
        if(maxi<numbers[i]):
            maxi=numbers[i]
    print(maxi)

maxlist2([2,4,6,23,14])
maxlist2([3,8,9,24,89])