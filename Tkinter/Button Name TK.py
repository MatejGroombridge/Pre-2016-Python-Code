

def name():
    print('whats your name?  my name is matej')

def matej():
    print('my name is matej')



from tkinter import *
t = Tk()
btn = Button(t, text="click here", command=name)
btn.pack()

