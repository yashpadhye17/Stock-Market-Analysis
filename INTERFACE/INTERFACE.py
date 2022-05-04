from tkinter import *
root=Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False, False)
Label(root,text="Python Registration Form",font="arial 25").pack(pady=50)
Label (text="Name", font=23).place(x=100, y=150)
Label(text="Phone", font=23).place(x=100, y=200)
Label(text="Gender", font=23).place(x=100, y=250)
Label(text="Email", font=23).place(x=100, y=300)
#entry
nameValue=StringVar()
phoneValue=StringVar()
genderValue=StringVar ()
emailValue=StringVar()

root.mainloop()