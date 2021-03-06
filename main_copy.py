# import tkinter as tk
# import cv2
# import imutils
# import main_support
# from PIL import Image, ImageTk
#
#
# class Toplevel1:
#     def __init__(self, top=None):
#         """This class configures and populates the toplevel window.
#         top is the toplevel containing window."""
#         _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
#         _fgcolor = "#000000"  # X11 color: 'black'
#         _compcolor = "#d9d9d9"  # X11 color: 'gray85'
#         _ana1color = "#d9d9d9"  # X11 color: 'gray85'
#         _ana2color = "#ececec"  # Closest X11 color: 'gray92'
#
#         top.geometry("1280x800+307+27")
#         top.minsize(120, 1)
#         top.maxsize(1280, 800)
#         top.resizable(1, 1)
#         top.title("Toplevel 0")
#         top.configure(background="#d9d9d9")
#         top.configure(highlightbackground="#d9d9d9")
#         top.configure(highlightcolor="black")
#
#         self.top = top
#         self.che46 = tk.IntVar()
#         self.che48 = tk.IntVar()
#         self.che53 = tk.IntVar()
#         self.che54 = tk.IntVar()
#         self.che55 = tk.IntVar()
#         self.che56 = tk.IntVar()
#         self.che57 = tk.IntVar()
#
#         self.Checkbutton1 = tk.Checkbutton(self.top)
#         self.Checkbutton1.place(relx=0.055, rely=0.075, relheight=0.031, relwidth=0.048)
#         self.Checkbutton1.configure(activebackground="#ececec")
#         self.Checkbutton1.configure(activeforeground="#000000")
#         self.Checkbutton1.configure(anchor="w")
#         self.Checkbutton1.configure(background="#d9d9d9")
#         self.Checkbutton1.configure(compound="left")
#         self.Checkbutton1.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton1.configure(foreground="#000000")
#         self.Checkbutton1.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton1.configure(highlightcolor="black")
#         self.Checkbutton1.configure(justify="left")
#         self.Checkbutton1.configure(text="""dwg""")
#         self.Checkbutton1.configure(variable=self.che46)
#
#         self.Checkbutton2 = tk.Checkbutton(self.top)
#         self.Checkbutton2.place(relx=0.095, rely=0.075, relheight=0.031, relwidth=0.051)
#         self.Checkbutton2.configure(activebackground="#ececec")
#         self.Checkbutton2.configure(activeforeground="#000000")
#         self.Checkbutton2.configure(anchor="w")
#         self.Checkbutton2.configure(background="#d9d9d9")
#         self.Checkbutton2.configure(compound="left")
#         self.Checkbutton2.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton2.configure(foreground="#000000")
#         self.Checkbutton2.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton2.configure(highlightcolor="black")
#         self.Checkbutton2.configure(justify="left")
#         self.Checkbutton2.configure(text="""bak""")
#         self.Checkbutton2.configure(variable=self.che48)
#
#         self.Checkbutton3 = tk.Checkbutton(self.top)
#         self.Checkbutton3.place(relx=0.133, rely=0.075, relheight=0.031, relwidth=0.051)
#         self.Checkbutton3.configure(activebackground="#ececec")
#         self.Checkbutton3.configure(activeforeground="#000000")
#         self.Checkbutton3.configure(anchor="w")
#         self.Checkbutton3.configure(background="#d9d9d9")
#         self.Checkbutton3.configure(compound="left")
#         self.Checkbutton3.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton3.configure(foreground="#000000")
#         self.Checkbutton3.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton3.configure(highlightcolor="black")
#         self.Checkbutton3.configure(justify="left")
#         self.Checkbutton3.configure(text="""step""")
#         self.Checkbutton3.configure(variable=self.che53)
#
#         self.Checkbutton4 = tk.Checkbutton(self.top)
#         self.Checkbutton4.place(relx=0.172, rely=0.075, relheight=0.031, relwidth=0.057)
#         self.Checkbutton4.configure(activebackground="#ececec")
#         self.Checkbutton4.configure(activeforeground="#000000")
#         self.Checkbutton4.configure(anchor="w")
#         self.Checkbutton4.configure(background="#d9d9d9")
#         self.Checkbutton4.configure(compound="left")
#         self.Checkbutton4.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton4.configure(foreground="#000000")
#         self.Checkbutton4.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton4.configure(highlightcolor="black")
#         self.Checkbutton4.configure(justify="left")
#         self.Checkbutton4.configure(text="""SLDASM""")
#         self.Checkbutton4.configure(variable=self.che54)
#
#         self.Checkbutton5 = tk.Checkbutton(self.top)
#         self.Checkbutton5.place(relx=0.227, rely=0.075, relheight=0.031, relwidth=0.057)
#         self.Checkbutton5.configure(activebackground="#ececec")
#         self.Checkbutton5.configure(activeforeground="#000000")
#         self.Checkbutton5.configure(anchor="w")
#         self.Checkbutton5.configure(background="#d9d9d9")
#         self.Checkbutton5.configure(compound="left")
#         self.Checkbutton5.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton5.configure(foreground="#000000")
#         self.Checkbutton5.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton5.configure(highlightcolor="black")
#         self.Checkbutton5.configure(justify="left")
#         self.Checkbutton5.configure(text="""SLDPRT""")
#         self.Checkbutton5.configure(variable=self.che55)
#
#         self.Checkbutton6 = tk.Checkbutton(self.top)
#         self.Checkbutton6.place(relx=0.055, rely=0.113, relheight=0.031, relwidth=0.052)
#         self.Checkbutton6.configure(activebackground="#ececec")
#         self.Checkbutton6.configure(activeforeground="#000000")
#         self.Checkbutton6.configure(anchor="w")
#         self.Checkbutton6.configure(background="#d9d9d9")
#         self.Checkbutton6.configure(compound="left")
#         self.Checkbutton6.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton6.configure(foreground="#000000")
#         self.Checkbutton6.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton6.configure(highlightcolor="black")
#         self.Checkbutton6.configure(justify="left")
#         self.Checkbutton6.configure(text="""mp4""")
#         self.Checkbutton6.configure(variable=self.che56)
#
#         self.Checkbutton7 = tk.Checkbutton(self.top)
#         self.Checkbutton7.place(relx=0.055, rely=0.15, relheight=0.031, relwidth=0.048)
#         self.Checkbutton7.configure(activebackground="#ececec")
#         self.Checkbutton7.configure(activeforeground="#000000")
#         self.Checkbutton7.configure(anchor="w")
#         self.Checkbutton7.configure(background="#d9d9d9")
#         self.Checkbutton7.configure(compound="left")
#         self.Checkbutton7.configure(disabledforeground="#a3a3a3")
#         self.Checkbutton7.configure(foreground="#000000")
#         self.Checkbutton7.configure(highlightbackground="#d9d9d9")
#         self.Checkbutton7.configure(highlightcolor="black")
#         self.Checkbutton7.configure(justify="left")
#         self.Checkbutton7.configure(text="""pdf""")
#         self.Checkbutton7.configure(variable=self.che57)
#
#         self.Labelframe1 = tk.LabelFrame(self.top)
#         self.Labelframe1.place(relx=0.055, rely=0.275, relheight=0.664, relwidth=0.535)
#         self.Labelframe1.configure(relief="groove")
#         self.Labelframe1.configure(font="-family {???????????????} -size 14 -weight bold")
#         self.Labelframe1.configure(foreground="black")
#         self.Labelframe1.configure(text="""????????????""")
#         self.Labelframe1.configure(background="#d9d9d9")
#         self.Labelframe1.configure(highlightbackground="#d9d9d9")
#         self.Labelframe1.configure(highlightcolor="black")
#
#         self.Label1 = tk.Label(self.Labelframe1)
#         self.Label1.place(
#             relx=0.029, rely=0.056, height=480, width=640, bordermode="ignore"
#         )
#         self.Label1.configure(activebackground="#f9f9f9")
#         self.Label1.configure(activeforeground="black")
#         self.Label1.configure(anchor="w")
#         self.Label1.configure(background="#d9d9d9")
#         self.Label1.configure(compound="left")
#         self.Label1.configure(disabledforeground="#a3a3a3")
#         self.Label1.configure(foreground="#000000")
#         self.Label1.configure(highlightbackground="#d9d9d9")
#         self.Label1.configure(highlightcolor="black")
#         self.Label1.configure(relief="ridge")
#         self.Label1.configure(text="""Label""")
#
#         self.Button1 = tk.Button(self.top)
#         self.Button1.place(relx=0.055, rely=0.2, height=34, width=128)
#         self.Button1.configure(activebackground="#ececec")
#         self.Button1.configure(activeforeground="#000000")
#         self.Button1.configure(background="#d9d9d9")
#         self.Button1.configure(compound="left")
#         self.Button1.configure(disabledforeground="#a3a3a3")
#         self.Button1.configure(foreground="#000000")
#         self.Button1.configure(highlightbackground="#d9d9d9")
#         self.Button1.configure(highlightcolor="black")
#         self.Button1.configure(pady="0")
#         self.Button1.configure(text="""Set Default""")
#         self.Button1.configure(command=self.button_event)
#
#     # ----------------------------------- ??????QRCode -----------------------------------
#     def load_cam(self):
#         global cam
#         if cam is not None:
#             ret, frame = cam.read()
#             if ret:
#                 frame = imutils.resize(frame, width=640, height=480)
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 frame = cv2.flip(frame, 1)
#
#                 img = Image.fromarray(frame)
#                 imgtk = ImageTk.PhotoImage(image=img)
#                 self.Label1.configure(image=imgtk)
#                 self.Label1.image = imgtk
#                 self.Label1.after(10, self.load_cam)
#
#     def iniciar(self):
#         global cam
#         cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#         self.load_cam()
#
#     # ----------------------------------- Button Event -----------------------------------
#     def button_event(self):
#         che1 = self.che46.get()
#         print(che1)
#
#
# def start_up():
#     main_support.main()
#
#
# if __name__ == "__main__":
#     main_support.main()
#Import tkinter library
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame or window
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x250")
def callback():
   Label(win, text="Hello World!", font=('Georgia 20 bold')).pack(pady=4)

#Create a Label and a Button widget
btn = ttk.Button(win, text="Press Enter to Show a Message", command= callback)
btn.pack(ipadx=10)

win.bind('<Return>',lambda event:callback())

win.mainloop()