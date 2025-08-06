#-------------------------------------- exception handling -----------------------------
# try--- code that may cause error are placed in this block
# except--- code to run when exception occurs
# else--- executed when the try block doesnot raise any exception
# finally--- always executed

# try:
#     num=10
#     deno=2
#     res=num/deno
#     # print(res)
# except:
#     print("denominator cannot be zero")
# else:
#     print(res)
# finally:
#     print("program closing...")



# try:
#     num=int(input("enter number : "))
#     assert num%2==0
# except:
#     print("not a even number")
# else:
#     reciprocal=1/num
#     print(reciprocal)
# finally:
#     print("the number was ",num)



try:
    with open('exception.csv','r') as f:
        context=f.read()
except FileNotFoundError:
    print("file not found in the directory")
else:
    print("file found!")
finally:
    print("closing program...")