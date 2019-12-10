from tkinter import *
master =Tk()
g_male=IntVar()
Checkbutton(master,text="male",variable=g_male).grid(row=0,sticky=W)
g_female=IntVar()
Checkbutton(master,text="female",variable=g_female).grid(row=1,sticky=W)
mainloop()
