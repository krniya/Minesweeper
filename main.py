from tkinter import *

root = Tk()

# Overriding the window settings
root.configure(bg="BLACK")
root.geometry('1440x720')
root.title('Minesweeper')
root.resizable(False,False)


top_frame = Frame(
    root,
    bg= 'red',
    width=1440,
    height=180,
)

top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=360,
    height=540
)

# Run the window
root.mainloop()