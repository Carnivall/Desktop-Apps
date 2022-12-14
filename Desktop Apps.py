from tkinter import *

root=Tk()
root.title("Apps")
root.geometry("400x500")


def hello():
    hello_label=Label(root,text="hello "+myTextbox.get())
    hello_label.pack()

myLabel= Label(root,text="enter your first name:")
myLabel.pack()

myTextbox=Entry(root, width=30)
myTextbox.pack()

myButton=Button(root, text="submit", command=hello)
myButton.pack()











    



















root.mainloop()