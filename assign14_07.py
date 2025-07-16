#print numbers from 1 to 10 using a for loop
for i in range(1,11):
    print(i)

print('--------------------------------')

#print even numbers between 1 and 20 using a while loop
i=2
while i<20:
    print(i)
    i+=2

print('--------------------------------')

#print the multiplication table of a number using for loop
x=int(input("enter the number:"))
for i in range(1,11):
    print(x*i)

print('--------------------------------')

#check if a number is prime using for loop
y=int(input("enter the number:"))
if y>0:
    for i in range(2,y):
        if(y%i==0):
            print("not a prime number")
            break
        else:
            print("prime number")
            break

print('--------------------------------')

#find factorial of a number using for loop
num=int(input("enter the number:"))
x=1
for i in range(1,num+1):
    x*=i
print(x)

print('--------------------------------')

#write a program to print numbers from 1 to 10.use break to stop when the number is 5
for i in range(1,11):
    if i==5:
        break
    print(i)

print('--------------------------------')

#print numbers from 1 to 10,skipping the number 7 using continue  
for i in range(1,11):
    if(i==7):
        continue
    print(i)
    
print('--------------------------------')

#print all numbers from 1 to 20,but skip numbers divisible by 3 using continue
for i in range(1,21):
    if(i%3==0):
        continue
    print(i)

    
print('--------------------------------')

#print numbers from 1 to 100.use break when the first number divisible by both 4 and 6 is found
for i in range(1,101):
    if i%4==0 and i%6==0:
        break
    print(i)


print('--------------------------------')

#print 1 to 100,skip 10 to 20:use continue to skip numbers
for i in range(1,101):
    if i>9 and i<21:
        continue
    print(i)

