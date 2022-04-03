import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('Gui 1')
label=ttk.Label(win,text='Click Me',font='Times 20',background='purple',foreground='yellow')
label.grid(column=0,row=0)
def clickMe():
    button.configure(text='Why did you click')
    label.configure(foreground='red')
button=ttk.Button(win,text='Alarm',command=clickMe)
button.grid(column=1,row=0)
win.mainloop()
