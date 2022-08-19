from tkinter import *
from tkinter.ttk import Button
import os
import time
import webbrowser


def callback(url):
    webbrowser.open_new_tab(url)


def restart():

    os.system("taskkill /im explorer.exe /f")
    time.sleep(3)
    os.system("start explorer.exe")


win1 = Tk()
win1.wm_attributes("-toolwindow", True)
win1.wm_attributes("-topmost", True)
win1.title("1-Click Restart Windows Desktop")
win1.geometry("285x95")
win1.resizable(False, False)
win1.eval("tk::PlaceWindow . center")

warning = Label(win1, text="Warning: Files being copied or moved may be lost.")
warning.grid(row=1, column=1, padx=5, sticky="n")


link = Label(win1, text="More apps by noteuclid", fg="blue", cursor="hand2")
link.grid(row=2, column=1, padx=5, sticky='ewn')
link.bind("<Button-1>", lambda e: callback("http://sourceforge.com/u/noteuclid"))

start = Button(win1, text="Restart", command=lambda: restart())
start.grid(row=3, column=1, pady=5, sticky='n')

win1.mainloop()
