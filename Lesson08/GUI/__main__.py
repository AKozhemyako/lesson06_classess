from tkinter import Tk, Button
if __name__ == '__main__':

    win = Tk()
    win.title("GUI on Python")
    win.geometry("300x250")

    btn = Button(text="buttonText",
                background="#555",
                foreground = "#ccc",
                width = "20", #Ширина кнопки
                underline = "0", #Подчеркиваем первую литеру на кнопке
                padx = "10",
                pady = "4",
                font = "10",
                )
    btn.pack()

    win.mainloop()
