# TS-19 05-03-2022
'''Try to configure the widget with various
options like: bg=”red”, family=”times”, 
size=18 
'''
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text='I am label widget',
fg='red',font='serif 20',bg='yellow')
label.pack()
root.title('My Window')
root.mainloop()
