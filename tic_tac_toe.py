from tkinter import *


root = Tk()

global counter 

counter = 0

def tic():
    global counter
    if counter%2 == 0:
        Button1ans = Button(root, padx=60, pady=50)
        Button1.place(x=15, y=0)
        Button1.config(text = "x")
    else: 
        Button1.config(text = "o")
    counter += 1

def tic2():
    global counter
    if counter%2 == 0:
        Button2ans = Button(root, padx=60, pady=50)
        Button2.place(x=180, y=0)
        Button2.config(text = "x")
    else: 
        Button2.config(text = "o")
    counter += 1

def tic3():
    global counter
    if counter%2 == 0:
        Button3ans = Button(root, padx=60, pady=50)
        Button3.place(x=340, y=0)
        Button3.config(text = "x")
    else: 
        Button3.config(text = "o")
    counter += 1

def tic4():
    global counter
    if counter%2 == 0:
        Button4ans = Button(root, padx=60, pady=50)
        Button4.place(x=15, y=120)
        Button4.config(text = "x")
    else: 
        Button4.config(text = "o")
    counter += 1

def tic5():
    global counter
    if counter%2 == 0:
        Button5ans = Button(root, padx=60, pady=50)
        Button5.place(x=180, y=120)
        Button5.config(text = "x")
    else: 
        Button5.config(text = "o")
    counter += 1

def tic6():
    global counter
    if counter%2 == 0:
        Button6ans = Button(root, padx=60, pady=50)
        Button6.place(x=340, y=120)
        Button6.config(text = "x")
    else: 
        Button6.config(text = "o")
    counter += 1

def tic7():
    global counter
    if counter%2 == 0:
        Button7ans = Button(root, padx=60, pady=50)
        Button7.place(x=15, y=230)
        Button7.config(text = "x")
    else: 
        Button7.config(text = "o")
    counter += 1

def tic8():
    global counter
    if counter%2 == 0:
        Button8ans = Button(root, padx=60, pady=50)
        Button8.place(x=180, y=230)
        Button8.config(text = "x")
    else: 
        Button8.config(text = "o")
    counter += 1

def tic9():
    global counter
    if counter%2 == 0:
        Button9ans = Button(root, padx=60, pady=50)
        Button9.place(x=340, y=230)
        Button9.config(text = "x")
    else: 
        Button9.config(text = "o")
    counter += 1


#define all buttons

Button1 = Button(root, padx=60, pady=50, command=tic)
Button2 = Button(root, padx=60, pady=50, command=tic2) 
Button3 = Button(root, padx=60, pady=50, command=tic3)
Button4 = Button(root, padx=60, pady=50, command=tic4)
Button5 = Button(root, padx=60, pady=50, command=tic5)
Button6 = Button(root, padx=60, pady=50, command=tic6)
Button7 = Button(root, padx=60, pady=50, command=tic7)
Button8 = Button(root, padx=60, pady=50, command=tic8)
Button9 = Button(root, padx=60, pady=50, command=tic9)



Button1.place(x=15, y=0)
Button2.place(x=180, y=0)
Button3.place(x=340, y=0)
Button4.place(x=15, y=120)
Button5.place(x=180, y=120)
Button6.place(x=340, y=120)
Button7.place(x=15, y=230)
Button8.place(x=180, y=230)
Button9.place(x=340, y=230)








root.geometry('500x375')
root.mainloop()
