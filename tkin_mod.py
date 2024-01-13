import tkinter
a=tkinter.Tk()
# a.geometry(400,400)
c=tkinter.Label(a,text='this is a GUI')
c.pack()
def fun():
     print(2+3)
b=tkinter.Button(a,text='press',command=fun)
b.pack()
a.mainloop()