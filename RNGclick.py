from tkinter import Tk, Label, StringVar
import random

def _quit():
    root.quit()    
    root.destroy()                 

def gen_rand(event):    
     
    randvar = random.randint(1,100)  
    tout.set(randvar) 
    
    if randvar < 25:
        label.config(fg='#FF3333')
    elif randvar < 50:
        label.config(fg='#FFAC33')
    elif randvar < 75:
        label.config(fg='#FFFF33')
    else:
        label.config(fg='#33FF39') 
		
    return 
 
def clear_rand(event):
 
	tout.set("")
	
	return
 
root = Tk()
root.title('RNG')
root.configure(background='black')
root.bind('<Button-1>', gen_rand)
root.bind('<Button-3>', clear_rand)
tout = StringVar()
label = Label(root, textvariable=tout, font=('TkDefaultFont', 100), bg='black')
label.pack()
root.mainloop()
