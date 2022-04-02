# TS-19 05-03-2022
'''
Try to change the widget type and configuration options to experiment with 
other widget types like Message, Button, Entry, Checkbutton, Radiobutton, 
Scale etc. '''

from tkinter import *
root=Tk()
root.title('I am a Top Level Widget, parent to other widgets')

# creating a frame (my_frame_1)
my_frame_1=Frame(root, bd=2, relief=SUNKEN)
my_frame_1.pack(side=LEFT)

# add check button widget to my_frame_1
Radiobutton(my_frame_1,text='Radio button Un',value=1).pack()
Radiobutton(my_frame_1,text='Radio button Dos',value=2).pack()
Radiobutton(my_frame_1,text='Radio button Tres',value=3).pack()
# adding my_image image
Label(my_frame_1,text='Image fun with Bitmap Class:').pack()
my_image=BitmapImage(file="gir.xbm")
my_label=Label(my_frame_1,image=my_image)
my_label.image=my_image #keep a referance!
my_label.pack()

# Frame2 and widgets it contains.
# Create another frame (my_frame_2) to hold a list box, Spinbox Widget, Scale Widget:
my_frame_2=Frame(root,bd=2, relief=GROOVE)
my_frame_2.pack(side=RIGHT)

# Scale Widget
Scale(my_frame_2, from_=0.0,to=100.0, label='Scale Widget', orient=HORIZONTAL).pack()
# Message Widget
Message(my_frame_2, text='I am message Widget').pack()

# Frame 4
#create another frame (my_frame_4)
my_frame_4 = Frame(root).pack ()
my_canvas = Canvas(my_frame_4, bg='white', width=340, height=80)
my_canvas.pack()
my_canvas.create_oval (200, 15, 60, 60, fill='red')
my_canvas.create_oval (40, 15, 90, 60, fill='grey')
my_canvas.create_text(130,38, text='I am Canvas Widget', font=('arial',8,'bold'))

root.mainloop()