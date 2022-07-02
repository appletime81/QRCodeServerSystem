import qrcode
import tkinter as tk
import qrcode_generator_support

from PIL import ImageTk
from tkinter import messagebox, filedialog


import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import qrcode_generator_support

class QRCodeGenerator:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black'
        _tabfg2 = 'black'
        _tabbg1 = 'grey75'
        _tabbg2 = 'grey89'
        _bgmode = 'light'

        top.geometry("1046x738+425+106")
        top.minsize(120, 1)
        top.maxsize(1046, 738)
        top.resizable(1,  1)
        top.title("QRCode產生器")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.che46 = tk.IntVar()

        self.generate_btn = tk.Button(self.top)
        self.generate_btn.place(relx=0.545, rely=0.054, height=44, width=168)
        self.generate_btn.configure(activebackground="beige")
        self.generate_btn.configure(activeforeground="#000000")
        self.generate_btn.configure(background="#d9d9d9")
        self.generate_btn.configure(compound='center')
        self.generate_btn.configure(disabledforeground="#a3a3a3")
        self.generate_btn.configure(font="-family {微軟正黑體} -size 19 -weight bold")
        self.generate_btn.configure(foreground="#000000")
        self.generate_btn.configure(highlightbackground="#d9d9d9")
        self.generate_btn.configure(highlightcolor="black")
        photo_location = "../Users/apple/Desktop/temp/button001.png"
        global _img0
        _img0 = tk.PhotoImage(file="button001.png")
        self.generate_btn.configure(image=_img0)
        self.generate_btn.configure(pady="0")
        self.generate_btn.configure(text='''生成QRCode''')

        self.save_btn = tk.Button(self.top)
        self.save_btn.place(relx=0.707, rely=0.054, height=44, width=168)
        self.save_btn.configure(activebackground="beige")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#d9d9d9")
        self.save_btn.configure(compound='center')
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {微軟正黑體} -size 19 -weight bold")
        self.save_btn.configure(foreground="#000000")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        photo_location = "../Users/apple/Desktop/temp/button002.png"
        global _img1
        _img1 = tk.PhotoImage(file="button002.png")
        self.save_btn.configure(image=_img1)
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''儲存檔案''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.057, rely=0.054, relheight=0.584
                , relwidth=0.446)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.064, rely=0.07, height=378, width=407)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.545, rely=0.203, relheight=0.493, relwidth=0.315)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Checkbutton1 = tk.Checkbutton(self.top)
        self.Checkbutton1.place(relx=0.631, rely=0.149, relheight=0.034
                , relwidth=0.134)
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {微軟正黑體} -size 14 -weight bold")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(selectcolor="#d9d9d9")
        self.Checkbutton1.configure(text='''是否含中文''')
        self.Checkbutton1.configure(variable=self.che46)

        # init parameter
        self.qr_image = None

        # bind button to function
        self.generate_btn.configure(command=self.generate_qrcode)
        self.save_btn.configure(command=self.save_qrcode)

    def generate_qrcode(self):
        # clear label image
        if self.Label1.cget("image") != "":
            print("clear image")
            self.Label1.configure(image=None)
            self.Label1.image = None

        info = self.Text1.get("1.0", tk.END).replace("\n", "")

        if info == "":
            messagebox.showwarning("警告", "請輸入資訊")
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # check checkbutton if it is checked
        if self.che46.get() == 1:
            info = "，" + info

        # set qr on label
        qr.add_data(info.encode("utf-8"))
        qr.make(fit=True)
        self.qr_image = qr.make_image()
        img = ImageTk.PhotoImage(qr.make_image().get_image().resize((407, 378)))
        self.Label1.configure(image=img)
        self.Label1.image = img
        self.Label1.pack()
        self.Label1.place(relx=0.5, rely=0.5, width=407, height=378, anchor="center")

    def save_qrcode(self):
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=[("PNG", "*.png")]
            )
            if filename == "":
                return
            self.qr_image.save(filename)
            messagebox.showinfo("成功", "QRCode已儲存")
        except:
            messagebox.showerror("錯誤", "QRCode儲存失敗")


def start_up():
    qrcode_generator_support.main()


if __name__ == "__main__":
    qrcode_generator_support.main()
