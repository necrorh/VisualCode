# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()
frame = Frame(window,bg="red",bd=5,relief=SUNKEN)
frame.place(x=100,y=100)
#frame.pack(side=RIGHT)
Button(frame,text="W",font=("Consolas",25),width=5).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=5).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=5).pack(side=RIGHT)
Button(frame,text="D",font=("Consolas",25),width=5).pack(side=BOTTOM)

window.mainloop()