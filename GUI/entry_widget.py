from tkinter import *
master = Tk() #master is an oject of Tk class type 
master.title("Entry Wizard")
Label(master,text="First Name",bg="Red").grid(row=0)
Label(master,text="Last Name").grid(row=1)
first=Entry(master)
second=Entry(master)
first.grid(row=0,column=1)
second.grid(row=1,column=1)

master1 = Tk() #master is an oject of Tk class type 
master1.title("Sony Wizard")
Label(master1,text="First Name",bg="Red").grid(row=0)
Label(master1,text="Last Name").grid(row=1)
first=Entry(master1)
second=Entry(master1)
first.grid(row=0,column=1)
second.grid(row=1,column=1)

mainloop()
