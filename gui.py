from tkinter import *
root=Tk()      #initializing window

#--------widgets--------

#name of window
root.title("Demo Window")

#dimension of window
root.geometry('800x400')

# #labels

# lbl1=Label(root,text="Welcome", font=('Lucida Handwriting',14),fg='black',bg='white')

# #label  position
# # using pack()
# # lbl1.pack()           #at top center
# #-----------------------------------------------------------------------------------------------------------------------------------
# # lbl=Label(root,text="Python Lobby")
# # lbl.pack(side=LEFT)
# # lbl.pack(side=RIGHT)
# # lbl.pack(side=TOP)
# # lbl.pack(side=BOTTOM)
# #-----------------------------------------------------------------------------------------------------------------------------------

# # using place()
# lbl1.place(x=350,y=300)

# # # entry widget - text whitespace
# # entry=Entry(root)
# # entry.place(x=200,y=100)

# entry1=Entry(root,width=50)
# entry1.place(x=400,y=50)


# # buttons

# # def clickme():
# #     print("i am clicked!!!")
# # btn = Button(root,text='click me',command=clickme)       #function name in command
# # btn.pack()                           #-------place and grid can be used together in a code!!!

# # window background color
root.config(bg='yellow')


# #image 
# path=PhotoImage(file='gui python/eeagle.png')
# label_image=Label(root, image=path)
# label_image.grid(row=4,column=2)



# #padding
# label2=Label(root,text='this is an image')#.pack(side=BOTTOM, pady=10,padx=10)


# #using grid for label position
# label2.grid(row=5,column=2)


# #checkbox

# cbox1=IntVar()
# cbox2=IntVar()
# cbox3=IntVar()

# button1=Checkbutton(root,text='reading',variable=cbox1,onvalue=1,offvalue=0,height=3, width=12)
# button1.pack()

# button2=Checkbutton(root,text='writing',variable=cbox2,onvalue=1,offvalue=0,height=3, width=12)
# button2.pack()
# button3=Checkbutton(root,text='learning',variable=cbox3,onvalue=1,offvalue=0,height=3, width=12)
# button3.pack()




# #Radio button
# demo=StringVar(root,"2")
# rbtn1=Radiobutton(root,text='option1',variable=demo,value='1')
# rbtn1.pack()
# rbtn2=Radiobutton(root,text='option2',variable=demo,value='2')
# rbtn2.pack()
# rbtn3=Radiobutton(root,text='option3',variable=demo,value='3')
# rbtn3.pack()



# #frame

# bframe=Frame(root,bg='red',width=120,height=100)
# bframe.pack(side=LEFT,padx=20)
# cframe=Frame(root,bg='green',width=120,height=100)
# cframe.pack(side=LEFT,padx=20)
# dframe=Frame(root,bg='blue',width=120,height=100)
# dframe.pack(side=LEFT,padx=20)



# #menu

# menubtn=Menubutton(root,text='gender',relief='raised',direction='below')
# menubtn.grid(padx=20,pady=20)

# menu=Menu(menubtn,tearoff=0)
# menubtn.config(menu=menu)

# menu.add_command(label='male',command=lambda:print("male"))
# menu.add_command(label='female',command=lambda:print("female"))
# menu.add_command(label='prefer not to say',command=lambda:print("[prefer not to say"))

# menu.add_separator()
# menu.add_command(label='exit',command=root.quit)



#Listbox

# listbox=Listbox(root,width=45,height=15)
# listbox.pack(pady=20)

# listbox.insert(0,'C')
# listbox.insert(0,'JAVA')
# listbox.insert(0,'C++')
# listbox.insert(0,'PYTHON')
# listbox.insert(0,'JS')

# TO CHOSE MULTIPLE VALUE IN LISTBOX

# listbox=Listbox(root,width=45,height=15,selectmode=MULTIPLE)
# listbox.pack(pady=20)

# listbox.insert(0,'C')
# listbox.insert(0,'JAVA')
# listbox.insert(0,'C++')
# listbox.insert(0,'PYTHON')
# listbox.insert(0,'JS')



root.mainloop()      #displaying window




#-------------------------------------------------------------------------------------------------------------------------------------------------


















































# #------------------------------------------------------------------------------------------------------------------------------------
# #                                           snapchat
# #------------------------------------------------------------------------------------------------------------------------------------

# from tkinter import *

# root = Tk()
# root.title("Snapchat Login")
# root.geometry("800x400")
# root.config(bg='gray')  


# left_frame = Frame(root, bg="#FFFC00", width=400, height=400)
# left_frame.place(x=0, y=0)


# logo_label = Label(left_frame, text="👻", font=("Arial", 24), bg="#FFFC00")
# logo_label.place(x=100, y=150)  # center-ish

# # ----- Right Panel (White) -----
# right_frame = Frame(root, bg="white", width=400, height=400)
# right_frame.place(x=400, y=0)

# # Title
# lbl1 = Label(right_frame, text="Log In", font=('Lucida Handwriting', 14), fg='black', bg='white')
# lbl1.place(x=150, y=30)

# # Username Entry
# entry1 = Entry(right_frame, width=40)
# entry1.place(x=50, y=80)

# # Password Entry
# entry2 = Entry(right_frame, width=40, show="*")
# entry2.place(x=50, y=130)

# # Button Function
# def clickme():
#     print("Login button clicked!")

# # Login Button
# btn = Button(right_frame, text='Log In', command=clickme)
# btn.place(x=150, y=180)

# root.mainloop()
