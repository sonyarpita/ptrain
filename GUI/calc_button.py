import tkinter as tk
import calculator as calcs
user_button=tk.Tk()
#user1_button=tk.Tk()
user_button.title("Creating a Button")
#user1_button.title("Quit a Button")
#button=tk.Button(user_button,text="Submit",width=50,command=user_button.destroy)
button=tk.Button(user_button,text="Calculate",width=50,command=calcs.sume)
button.pack()

button1=tk.Button(user_button,text="Quit",width=50,command=user_button.destroy)
button1.pack()

user_button.mainloop()
#user1_button.mainloop()
