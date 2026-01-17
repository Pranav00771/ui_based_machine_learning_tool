import tkinter as tk
from PIL import Image, ImageTk
import page_one
import webbrowser
class machine_tool:
 def get_ui():
   tt = tk.Tk()
   dx= tt.winfo_screenwidth()
   dy=tt.winfo_screenheight()
   tt.title("Machine Learning Tool")
   tt.geometry(("%dx%d")%(dx, dy))
   tt.attributes("-alpha", 0.9)
   tt.overrideredirect(1)
   tt.configure(bg="#004c99")
   img = Image.open("machine_tool_logo.jpg")
   img = img.resize((250, 250))
   global img1
   img1 = ImageTk.PhotoImage(img)
   lb_i = tk.Label(tt, image=img1, width="250", height="250")
   lb_i.place(x=10, y=10)
   close_b= tk.Label(tt, text="×", bg="#004c99", cursor="hand2", fg="#ffffff", font=("Calibri", 14))
   close_b.place(x=dx-100, y=10)
   def cbe(e):
    close_b.config(fg="#ff8000")
   def cbl(e):
     close_b.config(fg="#ffffff")
   def cbc(e):
       tt.destroy()
   close_b.bind('<Enter>',  cbe)
   close_b.bind('<Leave>', cbl)
   close_b.bind('<Button-1>', cbc)
   lbm = tk.Label(tt, text="Machine Learning Tool", bg="#004c99", fg="#ffffff", font=("Calibri", 29))
   lbm.place(x=400, y=10)
   btn = tk.Button(tt, text="Start", bg="#ffffff", fg="#000000", cursor="hand2", font=("Calibri", 14))
   btn.place(x=dx/2-100, y=dy/2-100)
   def bbe(e):
       btn.config(bg="#ff8000", fg="#ffffff")
   def bbl(e):
     btn.config(bg="#ffffff", fg="#000000")
   def bbc(e):
        btn.place_forget()
        page_one.page01.page1(tt)
   btn.bind('<Enter>',  bbe)
   btn.bind('<Leave>', bbl)
   btn.bind('<Button-1>', bbc)
   td = tk.Label(tt, text="Developer Pranav", bg="#004c99", fg="#ffffff", cursor="hand2", font=("Arial", 10))
   td.place(x=dx/2-100, y=dy-40)
   def tdc(e):
       webbrowser.open("https://github.com/Pranav00771")
   td.bind('<Button-1>',  tdc)
   tt.mainloop()


if __name__=="__main__":
  mt=machine_tool
  mt.get_ui()
  
   
   