import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm  import SVR
from sklearn.decomposition import PCA
from sklearn .cluster import KMeans
import page_four
class page03:
 @staticmethod
 def page3(tt, xtr, xts, ytr, yts):
    can1 = tk.Canvas(tt, width="600", height="400", bg="#ffffff")
    can1.place(x=tt.winfo_screenwidth()/2-300, y=tt.winfo_screenheight()/2-150)
    txt1 = tk.Label(can1, text="Select Algorithm:", bg="#ffffff", fg="#000000")
    txt1.place(x=20, y=100)
    combo1 = ttk.Combobox(can1, values=["Linear Regression", "Logistic Regression",  "Support Vector Machine","K-Means", "Principal Component Analysis", "Random Forest", "Gradient Boosting"], font=("Arial", 22))
    combo1.place(x=120, y=100)
    predict_btn = tk.Label(can1, text="Fit & Predict", bg="#004c99", fg="#ffffff", cursor="hand2")
    predict_btn.place(x=450, y=300)
    def predict_f(e):
         if combo1.get().lower()=="linear regression":
                  reg = LinearRegression()
                  xtr1=np.array(xtr).reshape(-1, 1)
                  ytr1=np.array(ytr).reshape(-1, 1)
                  xts1=np.array(xts).reshape(-1, 1)
                  yts1=np.array(yts).reshape(-1, 1)
                  reg.fit(xtr1, ytr1)
                  pred1 = reg.predict(xts1)
                  page_four.page04.page4(tt, yts1, pred1)
         elif combo1.get().lower()=="support vector machine":
                  svr=SVR(kernel='linear')
                  xtr1=np.array(xtr).reshape(-1, 1)
                  ytr1=np.array(ytr).reshape(-1, 1).ravel()
                  xts1=np.array(xts).reshape(-1, 1)
                  yts1=np.array(yts).reshape(-1, 1)
                  svr.fit(xtr1, ytr1)
                  pred1 = svr.predict(xts1)
                  page_four.page04.page4(tt, yts1,  pred1)
         elif combo1.get().lower()=="principal component analysis":
                  pca=PCA()
                  xtr1=np.array(xtr).reshape(-1, 1)
                  ytr1=np.array(ytr).reshape(-1, 1).ravel()
                  xts1=np.array(xts).reshape(-1, 1)
                  yts1=np.array(yts).reshape(-1, 1)
                  pred1= pca.fit_transform(xtr1)
                  page_four.page04.page4(tt, yts1,  pred1)
         elif combo1.get().lower()=="k-means":
                  xtr1=np.array(xtr)
                  ytr1=np.array(ytr)
                  yts1=np.array(yts)
                  data=list(zip(xtr1, ytr1))
                  inertias=[]
                  for x in range(1, 11):
                        kmeans=KMeans(n_clusters=x)
                        kmeans.fit(data)
                        inertias.append(kmeans.inertia_)
                  pred1=inertias
                  page_four.page04.page4(tt, range(1, 11), pred1)
         elif combo1.get().lower()=="logistic regression":
                  reg = LogisticRegression()
                  xtr1=np.array(xtr).reshape(-1, 1).astype(int)
                  ytr1=np.array(ytr).reshape(-1, 1).astype(int)
                  xts1=np.array(xts).reshape(-1, 1).astype(int)
                  yts1=np.array(yts).reshape(-1, 1).ravel()
                  reg.fit(xtr1, ytr1)
                  pred1=reg.predict(xts1)
                  page_four.page04.page4(tt, yts1, pred1)
         elif combo1.get().lower()=="random forest":
                  rfr = RandomForestRegressor(n_estimators=100)
                  xtr1=np.array(xtr).reshape(-1, 1).astype(int)
                  ytr1=np.array(ytr).reshape(-1, 1).astype(int)
                  xts1=np.array(xts).reshape(-1, 1)
                  yts1=np.array(yts).reshape(-1, 1).ravel()
                  rfr.fit(xtr1, ytr1)
                  pred1=rfr.predict(xts1)
                  page_four.page04.page4(tt, yts1, pred1)
         elif combo1.get().lower()=="gradient boosting":
                  gbr = GradientBoostingRegressor(n_estimators=100)
                  xtr1=np.array(xtr).reshape(-1, 1)
                  ytr1=np.array(ytr).reshape(-1, 1)
                  xts1=np.array(xts).reshape(-1, 1)
                  yts1=np.array(yts).reshape(-1, 1).ravel()
                  gbr.fit(xtr1, ytr1)
                  pred1=gbr.predict(xts1)
                  page_four.page04.page4(tt, yts1, pred1)
    predict_btn.bind('<Button-1>', predict_f)
   
    