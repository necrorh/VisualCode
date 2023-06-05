from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    #messagebox.showinfo(title='This is an info message box',message='you are a person')
    #messagebox.showwarning(title='WARNING',message='you have a virus')
    #messagebox.showerror(title='ERROR!',message='Something went wrong :()')

    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
    #    print('you did the thing!')
    #else:
    #    print('you canceled a thing! :(')
    
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing?'):
    #    print('you retried the thing!')
    #else:
    #    print('you canceled a thing! :(')
    
    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #    print('I like cake too')
    #else:
    #    print('I hate youuuuuuuuu!')

    #answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    #if(answer == 'yes'):
    #    print('I like pie too :)')
    #else(answer == 'no'):
    #    print('Kill yourself!!!!!!!!')

    answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='warning') #error#info
    if(answer==True):
        print("You like to code :)))")
    elif(answer==False):
        print("Then why tf are you watching a video on coding?")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()