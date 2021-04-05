import tkinter as tk  # Импортируем Tkinter для нашего приложения


class Main(tk.Frame):  # Создаем класс для нашего приложения и контейнер Frame
    def __init__(self, root):  #
        super().__init__(root)  # Передаем инит для рута методом супер
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg="#44036F", bd=2)  # Добавим тулбар
        toolbar.pack(side=tk.TOP, fill=tk.X)  # Ставим тулбар в верху основного окна


if __name__ == '__main__':
    root = tk.Tk()  # Создадим коренвое окно программы
    app = Main(root)  # Будем создавать основное окно нашей программы
    app.pack()  # Упасковка содержимого методом pack
    root.title("Kinоmania")  # Названия нашей программы и его основное окно
    root.geometry("650x450+300+200")  # Зададим размер окна и расположение на экране
    root.resizable(False, False)  # Отключаем изменение размеров основного окна программы
    root.mainloop()  # Запуск приложения.
