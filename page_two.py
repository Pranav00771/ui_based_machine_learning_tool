import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import page_three
class page02:
 @staticmethod
 def page2(tt, dataset):
    can1 = tk.Canvas(tt, width="600", height="400", bg="#ffffff")
    can1.place(x=tt.winfo_screenwidth()/2-300, y=tt.winfo_screenheight()/2-150)
    note1=tk.Label(can1, text="Please select numerical data as target :", bg="#ffffff", fg="#004c99", font=("Calibri", 12))
    note1.place(x=200, y=20)
    txt1= tk.Label(can1, text="X-Param :", bg="#ffffff", fg="#000000")
    txt1.place(x=200, y=100)
    txt2= tk.Label(can1, text="Y-Param :", bg="#ffffff", fg="#000000")
    txt2.place(x=200, y=140)
    txt3= tk.Label(can1, text="Test Size:", bg="#ffffff", fg="#000000")
    txt3.place(x=200, y=180)
    col1 = tk.StringVar()
    col2  = tk.StringVar()
    test1=tk.StringVar()
    txt_1= tk.Entry(can1, textvariable=col1, bg="#ffffff", fg="#000000")
    txt_1.place(x=300, y=100)
    txt_2= tk.Entry(can1, textvariable=col2, bg="#ffffff", fg="#000000")
    txt_2.place(x=300, y=140)
    txt_3= tk.Entry(can1, width="4", textvariable=test1, bg="#ffffff", fg="#000000")
    txt_3.place(x=300, y=180)
    next_btn = tk.Label(can1, text="Next", bg="#004c99", fg="#ffffff", cursor="hand2")
    next_btn.place(x=450, y=300)
    def next1(e):
      if len(col1.get())>0 and len(col2.get())>0 and len(test1.get())>0:
               x=dataset[col1.get()]
               y=dataset[col2.get()]
               x_train, x_test, y_train, y_test=  train_test_split(x, y, random_state=140, test_size=float(test1.get()))
               can1.place_forget()
               page_three.page03.page3(tt, x_train, x_test, y_train, y_test)
    next_btn.bind('<Button-1>', next1)
    
    
    
    