def submit():
    
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    # print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

from tkinter import *


window = Tk()
listbox = Listbox(window,
                bg='yellow',
                fg='black',
                font=('constantia',35),
                width=20,
                selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(1, "Pasta")
listbox.insert(1, "Garlic Bread")
listbox.insert(1, "Soup")
listbox.insert(1, "Salad")

listbox.config(height=listbox.size())
entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit",command=submit)
submitButton.pack()

addButton = Button(window, text="add",command=add)
addButton.pack()

deleteButton = Button(window, text="delete",command=delete)
deleteButton.pack()

window.mainloop()
