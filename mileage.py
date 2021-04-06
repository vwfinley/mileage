#!/usr/bin/env python

# Some helpful links
# https://docs.python.org/3/library/tkinter.html
# https://www.python-course.eu/tkinter_entry_widgets.php

import tkinter as tk

class Application(tk.Frame):
    
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root

        self.root.title("Mileage")
        self.root.geometry("250x125")        
        self.pack()
        
        self.miles = tk.Entry(self);
        self.gallons = tk.Entry(self);
        self.mpg = tk.Label(self)
        
        self.init_widgets()       

    def init_widgets(self):
        self.miles.grid(row=0)
        tk.Label(self, text="Miles").grid(row=0, column=1)

        self.gallons.grid(row=1)
        tk.Label(self, text="Gallons").grid(row=1, column=1)

        self.mpg.grid(row=2)
        tk.Label(self, text="MPG").grid(row=2, column=1)
        
        tk.Button(self, text="Calculate", command = self.calculate).grid(row=3, column=1)
        tk.Button(self, text="Quit", command=self.master.destroy).grid(row=4, column=1)

    def calculate(self):
        self.mpg['text'] = float(self.miles.get()) / float(self.gallons.get())


app = Application(root=tk.Tk())
app.mainloop()
