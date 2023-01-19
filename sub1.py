from tkinter import *
from tkinter import ttk


class createScrolableFrame:
    def __init__(self, parrentFrame, scrolableFrame):
        self.parrentFrame = parrentFrame
        self.scrolableFrame = scrolableFrame
        self.my_canvas = "my_canvas"
        self.createFrame()

    def createFrame(self):
        main_frame = LabelFrame(self.parrentFrame, width=790, height=710)
        main_frame.pack( anchor=CENTER, padx=10, pady=10)
        self.my_canvas = Canvas(main_frame, width=800, height=720)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        self.my_canvas.configure(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
        self.scrolableFrame = Frame(self.my_canvas)
        self.scrolableFrame.place(x=0, y=0)
        self.my_canvas.create_window((0, 0), window=self.scrolableFrame, anchor="nw")







