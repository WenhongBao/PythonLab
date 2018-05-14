from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def _init_(self,master=None):
        Frame._init_(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,Text='Hello',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app=Application()
app.master.title('Hello world')
app.mainloop()
