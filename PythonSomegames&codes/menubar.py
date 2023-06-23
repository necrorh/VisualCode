from tkinter import * 

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text!")
def copy():
    print("You copied some text!")
def paste():
    print("You pasted some text!")

window = Tk()

menubar = Menu(window) # Creates a menu bar
window.config(menu=menubar) 

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10)) # Creates a drop down menu
menubar.add_cascade(label="File",menu=fileMenu) # Adds a drop down menu
fileMenu.add_command(label="Open",command=openFile) # Adds a command to the drop down menu
fileMenu.add_command(label="Save",command=saveFile) # Adds a command to the drop down menu    
fileMenu.add_separator() # Adds a line to separate the commands
fileMenu.add_command(label="Exit",command=quit) # Adds a command to the drop down menu     

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10)) 
menubar.add_cascade(label="Edit",menu=editMenu)     
editMenu.add_command(label="Cut",command=cut) 
editMenu.add_command(label="Copy",command=copy) 
editMenu.add_command(label="Paste",command=paste)   

window.mainloop()