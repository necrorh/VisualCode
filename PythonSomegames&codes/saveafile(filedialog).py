from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\berkk\\Desktop",
                                    defaultextension='.txt',
                                    filetypes=[("text files","*.txt"),
                                                ("HTML files","*.html"),
                                                ("all files","*.*"),
                                    ])
    if file is None:
        return
    #filetext = str(text.get("1.0",END))
    filetext = input("Enter some text i guess: ") #konsoldan yazı yazmak için
    file.write(filetext)
    file.close()
window = Tk()
button = Button(text="Save",command=saveFile)
button.pack()
text = Text(window)
text.pack()



window.mainloop()