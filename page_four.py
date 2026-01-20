import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
class page04:
 @staticmethod
 def page4(tt, ytest,  pred):
    can1 = tk.Canvas(tt, width="600", height="400", bg="#ffffff")
    can1.place(x=tt.winfo_screenwidth()/2-300, y=tt.winfo_screenheight()/2-150)
    title1 = tk.StringVar()
    xlab1=tk.StringVar()
    ylab1=tk.StringVar()
    lab_1 = tk.Label(can1, text="Title:", bg="#ffffff", fg="#000000")
    lab_1.place(x=100, y=80)
    et1 = tk.Entry(can1, textvariable=title1)
    et1.place(x=140, y=80)
    lab_2 = tk.Label(can1, text="X-Axis:", bg="#ffffff", fg="#000000")
    lab_2.place(x=100, y=120)
    et2 = tk.Entry(can1, textvariable=xlab1)
    et2.place(x=160, y=120)
    lab_3= tk.Label(can1, text="Y-Axis:", bg="#ffffff", fg="#000000")
    lab_3.place(x=100, y=160)
    et2 = tk.Entry(can1, textvariable=ylab1)
    et2.place(x=160, y=160)
    lab1 = tk.Label(can1, text="Plot Type:", bg="#ffffff", fg="#000000")
    lab1.place(x=100, y=220)
    combo2 = ttk.Combobox(can1, values=["Line Plot", "Scatter Plot", "Hist Plot"])
    combo2.place(x=160, y=220)
    plot_btn = tk.Label(can1, text="Plot", bg="#004c99", fg="#ffffff", cursor="hand2")
    plot_btn.place(x=400, y=300)
    def plot1(e):
      if combo2.get().lower()=="line plot":
             if len(title1.get())>0 and len(xlab1.get())>0 and len(ylab1.get())>0:
              plt.plot(ytest, pred)
              plt.title(title1.get())
              plt.xlabel(xlab1.get())
              plt.ylabel(ylab1.get())
              plt.show()
      elif combo2.get().lower()=="scatter plot":
            if len(title1.get())>0 and len(xlab1.get())>0 and len(ylab1.get())>0:
              plt.scatter(ytest, pred)
              plt.title(title1.get())
              plt.xlabel(xlab1.get())
              plt.ylabel(ylab1.get())
              plt.show()
      elif combo2.get().lower()=="hist plot":
            if len(title1.get())>0 and len(xlab1.get())>0 and len(ylab1.get())>0:
              plt.hist(pred)
              plt.title(title1.get())
              plt.xlabel(xlab1.get())
              plt.ylabel(ylab1.get())
              plt.show()      
    plot_btn.bind('<Button-1>', plot1)
    scm_btn = tk.Label(can1, text="Scores & Confusion Matrix", bg="#004c99", fg="#ffffff", cursor="hand2")
    scm_btn.place(x=450, y=300)
    def scm1(e):
              ytrue=np.zeros_like(ytest)
              pred1= np.zeros_like(pred)
              acc1=metrics.accuracy_score(ytrue, pred1)
              cm1 = metrics.confusion_matrix(ytrue, pred1)
              pre1 = metrics.precision_score(ytrue, pred1)
              recall1= metrics.recall_score(ytrue, pred1)
              acc_str = "Accuracy Score : "+str(acc1)
              cm_str = "Confusion Matrix : "+str(cm1)
              pre_str ="Precision Score : "+str(pre1)
              recall_str = "Recall Score : "+str(recall1)
              lb1 = tk.Label(can1, text=acc_str, bg="#ffffff", fg="#000000")
              lb1.place(x=450, y=100)
              lb2 = tk.Label(can1, text=cm_str, bg="#ffffff", fg="#000000")
              lb2.place(x=450, y=120)
              lb3 = tk.Label(can1, text=pre_str, bg="#ffffff", fg="#000000")
              lb3.place(x=450, y=140)
              lb4 = tk.Label(can1, text=recall_str, bg="#ffffff", fg="#000000")
              lb4.place(x=450, y=160)
    scm_btn.bind('<Button-1>', scm1)

