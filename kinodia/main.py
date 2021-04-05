import tkinter as tk  # Импортируем Tkinter для нашего приложения


class Main(tk.Frame):  # Создаем класс для нашего приложения и контейнер Frame
    def __init__(self, root):  #
        super().__init__(root)  # Передаем инит для рута методом супер
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg="#44036F", bd=2)  # Добавим тулбар
        toolbar.pack(side=tk.TOP, fill=tk.X)  # Ставим тулбар в верху основного окна

        self.add_img = tk.PhotoImage(file="React.png") #Добавляю иконку по которой буду кликать и добавлять киношку
        btn_open_dialog = tk.Button(toolbar, text="Добавим новый Фильм", command=self.open_dialog, bg="#FFE100", bd=0,
                                    compound=tk.TOP, image=self.add_img) #Добавим кнопку с тесктом на тулбар
        btn_open_dialog.pack(side=tk.LEFT)

    def open_dialog(self): # Вызов дочернего окна
        Child()

class Child(tk.Toplevel): # Создадим дочернее окно для ввода данных в форму
    def __init__(self): # Создаем конструктор класса
        super().__init__(root) # Добавляем метод
        self.init_child()

    def init_child(self):  #Добавляем объект и виджет дочернего окошка
        self.title("Добавь новый фильм!") #Титутлка дочернего окна
        self.geometry("450x400+200+200") # Типоразмеры
        self.resizable(False, False) # Отключаем изменение размеров окна
        self.grab_set()
        self.focus_set()

if __name__ == '__main__':
    root = tk.Tk()  # Создадим коренвое окно программы
    app = Main(root)  # Будем создавать основное окно нашей программы
    app.pack()  # Упасковка содержимого методом pack
    root.title("Kinоmania")  # Названия нашей программы и его основное окно
    root.geometry("650x450+300+200")  # Зададим размер окна и расположение на экране
    root.resizable(False, False)  # Отключаем изменение размеров основного окна программы
    root.mainloop()  # Запуск приложения.
