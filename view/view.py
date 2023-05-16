import tkinter as tk
import xml.etree.ElementTree as et


class MyWindow:
    def __init__(self, win):
        self.lbl1 = tk.Label(win, text='First number')
        self.lbl2 = tk.Label(win, text='Second number')
        self.lbl3 = tk.Label(win, text='Result')
        self.t1 = tk.Entry(bd=3)
        self.t2 = tk.Entry()
        self.t3 = tk.Entry()
        self.btn1 = tk.Button(win, text='Add')
        self.btn2 = tk.Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1 = tk.Button(win, text='Add', command=self.add)
        self.b2 = tk.Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(tk.END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(tk.END, str(result))


if __name__ == "__main__":
    #Get strings
    tree = et.parse('../data/strings.xml')
    root = tree.getroot()

    #Create window
    window = tk.Tk()
    mywin = MyWindow(window)
    window.title(f"{root[0].text} {root[1].text}")
    window.geometry("400x300+10+10")
    window.mainloop()
