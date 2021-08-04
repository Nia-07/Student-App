from tkinter import Tk, Canvas, Label, Frame, Entry

import atexit


root = Tk()
root.title("python y PostgreSQL")

# Canvas
Canvas(root,height=380, widt=400)


frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label (frame, text="Add A student")
label.grid(row=0, column=1)

label = Label (frame, text="NAME")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

atexit.register(root.mainloop)  
