from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(relx=.3, rely=.1, anchor="e", height=30, width=130, bordermode=OUTSIDE)



root.mainloop()