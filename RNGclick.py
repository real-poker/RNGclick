import tkinter as tk
import random

colorSwitch = True
lowLim = 1
hiLim = 100
def gen_rand(event):  
    global colorSwitch
    global lowLim, hiLim
    randvar = random.randint(lowLim,hiLim)  
    tout.set(randvar) 
    
    if colorSwitch:
        if lowLim == 0:
            if randvar < 25:
                label.config(fg='#FF3333')
            elif randvar < 50:
                label.config(fg='#FFAC33')
            elif randvar < 75:
                label.config(fg='#FFFF33')
            else:
                label.config(fg='#33FF39') 
        else:
            if randvar < 26:
                label.config(fg='#FF3333')
            elif randvar < 51:
                label.config(fg='#FFAC33')
            elif randvar < 76:
                label.config(fg='#FFFF33')
            else:
                label.config(fg='#33FF39') 
    else:
        if lowLim == 0:
            if randvar < 25:
                label.config(fg='#33FF39')
            elif randvar < 50:
                label.config(fg='#FFFF33')
            elif randvar < 75:
                label.config(fg='#FFAC33')
            else:
                label.config(fg='#FF3333') 
        else:
            if randvar < 26:
                label.config(fg='#33FF39')
            elif randvar < 51:
                label.config(fg='#FFFF33')
            elif randvar < 76:
                label.config(fg='#FFAC33')
            else:
                label.config(fg='#FF3333')   
                             
def clear_rand(event):
	tout.set("")

def cSwitch():
    global colorSwitch
    colorSwitch = not(colorSwitch)
    
def rng99():
    global lowLim, hiLim
    lowLim = 0
    hiLim = 99
    
def rng100():
    global lowLim, hiLim
    lowLim = 1
    hiLim = 100  
    
root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="Switch Colour Ranking", command=cSwitch)
filemenu.add_separator()
filemenu.add_command(label="RNG from 0-99", command=rng99)
filemenu.add_command(label="RNG from 1-100", command=rng100)

menubar.add_cascade(label="Options", menu=filemenu)
root.title('RNG')
root.configure(background='black')
root.config(menu=menubar)
root.bind('<Button-1>', gen_rand)
root.bind('<Button-3>', clear_rand)
tout = tk.StringVar()
label = tk.Label(root, textvariable=tout, font=('Consolas', 100), bg='black')
label.pack(side="top", fill="both")
root.geometry("220x140+200+200")
root.mainloop()
