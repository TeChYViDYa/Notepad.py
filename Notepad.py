
''' Hello guys, i am techy vidya, creator of this notepad, I know that this is not difficult to make but 
then also it's mine , i hope you have got everything you wanted whether it is the code or really you wanted
my notepad from here , lastly but not the least thank you'''

# Some imports 

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# root object of the notepad

root = Tk()

# initializing the  window - root

root_size = "800x600"
root.title("Untitled - Notepad")
root.wm_iconbitmap("Notepad2.ico")
root.geometry(root_size)

# functions for File menu bar
def Newfunc():
    global file 
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def Openfunc():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes =[ ("All Types", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def Savefunc():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt" ,defaultextension = ".txt", filetypes =[ ("All Types", "*.*"),("Text Documents", "*.txt")])
        root.title(os.path.basename(file) + " -Notepad")
        print(file)
        f = open(file, "x")
        g = textArea.get(1.0, END)
        f.write(g)
        f.close()
        
    else:
        print("hello")
        f = open(file, "w")
        g = textArea.get(1.0, END)
        f.write(g)
        f.close()

# functions for helpMenu bar

def Cutfunc():
    textArea.event_generate("<<Cut>>")

def Copyfunc():
    textArea.event_generate("<<Copy>>")

def Pastefunc():
    textArea.event_generate("<<Paste>>")

# function for about menu bar

def Aboutfunc():
    showinfo("Notepad", "This Notepad has been created by a very good boy whose name is Techy Vidya, i hope you are enjoying my notepad , by the way i have created this in 2021, and what is the year going on now")

# File object for Notepad

file = None

# Creating the text area for our notepad

textArea = Text(root, font = "Lucida 13 italic")
textArea.pack(fill = BOTH, expand = True)

# creating the horizontal tab for menubars

MenuBar = Menu(root)

# filemenu starts
FileMenu = Menu(MenuBar, tearoff = 0)
FileMenu.add_command(label = "New", command = Newfunc)
FileMenu.add_command(label = "Open", command = Openfunc)
FileMenu.add_separator()
FileMenu.add_command(label = "Save", command = Savefunc)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quit)
MenuBar.add_cascade(label = "File", menu = FileMenu)
# fileMenu ends

# Edit menu starts

EditMenu = Menu(MenuBar, tearoff = 0)
EditMenu.add_command(label = "Cut", command = Cutfunc)
EditMenu.add_command(label = "Copy", command = Copyfunc)
EditMenu.add_command(label = "Paste", command = Pastefunc)
MenuBar.add_cascade(label = "Edit", menu = EditMenu)

# Edit menu ends

# Help menu starts

HelpMenu = Menu(MenuBar, tearoff = 0)
HelpMenu.add_command(label = "About Notepad", command = Aboutfunc)
MenuBar.add_cascade(label = "Help", menu = HelpMenu)

# configuring the root with the menubar

root.config(menu = MenuBar)

# adding scroll bar
scrollbar = Scrollbar(textArea)
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.config(command = textArea.yview)
textArea.config(yscrollcommand= scrollbar.set)

# mainloop
root.mainloop()