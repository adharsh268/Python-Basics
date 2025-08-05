#----------------- txt file ----------------
#write-w           #read-r           #append-a              #create-x


#open
# f=open('hello.txt','w')
# f.write("hello i am bob")
# f.close()

# f=open('hello.txt','r')
# print(f.read())
# f.close()



# with open
# with open('hello1.txt','w') as f:
#     f.write("hello i am daksh")

# with open('hello1.txt','w') as f:      #the first line will be deleted automatically
#     f.write("i am 21 yrs old")

# with open('hello1.txt','a') as f:
#     f.write("my name is daksh")

# with open('hello1.txt') as f:
#     print(f.read())




#writelines( ) method

# f=open('file1.txt','w')
# f.write("hello i am bob")
# f.close()

# f=open('file1.txt','a')
# f.writelines(['\nhello i am','\tadharsh\n. i am','\t21 yrs old'])
# f.close()

# f=open('file1.txt','r')
# print(f.read())
# f.close()




#readlines() method

# f=open('file1.txt','r')
# print(f.readlines(5))
# f.close()




# f=open('file2.txt','w')
# f.write("hello i am bob")
# f.close()

# f=open('file1.txt','r')
# print(f.read(9))
# f.close()






#----------------- csv file --------------------


# #write
# import csv
# with open('file1.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['sno.','name','age'])
#     w.writerow([1,'bob',21])
#     w.writerow([2,'nakul',24])


# #read
# import csv
# with open('file1.csv','r') as f:
#     r=csv.reader(f)
#     for row in r:
#         print(row)


# #append
# import csv
# new_row=[3,'daksh',23]
# with open('file1.csv','a',newline='')as f:
#     a=csv.writer(f)
#     a.writerow(new_row)


# import csv
# with open('file1.csv','r') as f:
#     r=csv.reader(f)
#     for row in r:
#         print(row)







#----------------- zip file ---------------------

#zipping-----write
import zipfile
with zipfile.ZipFile('com.zip','w') as f:
    f.write('file1.csv')                #files to be zipped
    f.write('example.py')

#unzip-------extract/read
import zipfile
with zipfile.ZipFile('com.zip','r') as f:
    f.extractall('extracted_file')         #extracted file location
    list1=f.namelist()
    print(list1)
