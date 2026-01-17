import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import page_two
class page01:
 @staticmethod
 def page1(tt):
    can1 = tk.Canvas(tt, width="600", height="400", bg="#ffffff")
    can1.place(x=tt.winfo_screenwidth()/2-300, y=tt.winfo_screenheight()/2-150)
    text1 = tk.Label(can1, text="", bg="#ffffff", fg="#000000", font=("Calibri", 12))
    text1.place(x=350, y=200)
    imp_btn = tk.Label(can1, text="Import Dataset", bg="#004c99", fg="#ffffff", cursor="hand2")
    imp_btn.place(x=250, y=200)
    def ibc(e):
        path1=filedialog.askopenfilename(title="Open Dataset", filetypes=[("CSV Files", ".csv")])
        if len(path1)>0:
            dir1, file1 = os.path.split(path1)
            text1.config(text=file1)
            dataset = pd.read_csv(path1)
            next_btn = tk.Label(can1, text="Next", bg="#004c99", fg="#ffffff", cursor="hand2")
            next_btn.place(x=450, y=300)
            def next1(e):
               can1.place_forget()
               page_two.page02.page2(tt, dataset)
            next_btn.bind('<Button-1>', next1)
    imp_btn.bind('<Button>', ibc)