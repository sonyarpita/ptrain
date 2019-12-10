import tkinter as tk
user_button=tk.Tk()
user_button.title("Creating a Button")
button=tk.Button(user_button,text="Submit",width=50,command=user_button.destroy)
button.pack()
user_button.mainloop()
