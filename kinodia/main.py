import tkinter as tk  # Импортируем Tkinter для нашего приложения
from tkinter import ttk  # Добавим виджет для отображение базы данных превью
import sqlite3
import datetime as dt
import data as data


class Main(tk.Frame):  # Создаем класс для нашего приложения и контейнер Frame
    def __init__(self, root) -> object:  #
        super().__init__(root)  # Передаем инит для рута методом супер
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg="#44036F", bd=2)  # Добавим тулбар
        toolbar.pack(side=tk.TOP, fill=tk.X)  # Ставим тулбар в верху основного окна

        self.add_img = tk.PhotoImage(file="React.png")  # Добавляю иконку по которой буду кликать и добавлять киношку
        btn_open_dialog = tk.Button(toolbar, text="Добавим новый Фильм", command=self.open_dialog, bg="#FFE100", bd=0,
                                    compound=tk.TOP, image=self.add_img)  # Добавим кнопку с тесктом на тулбар
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=("ID", "Film name", "Year", "Genre", "Time", "Regisseur", "Artist"),
                                 height=35,
                                 show="headings")  # Тот же виджет превью уже на основное окно и наши колонки что
        # будем заполнять
        # Размещаем на первом окне виджет и центрируем по центру названия колонок таблицы
        self.tree.column("ID", width=55, anchor=tk.CENTER)
        self.tree.column("Film name", width=185, anchor=tk.CENTER)
        self.tree.column("Year", width=60, anchor=tk.CENTER)
        self.tree.column("Genre", width=60, anchor=tk.CENTER)
        self.tree.column("Time", width=60, anchor=tk.CENTER)
        self.tree.column('Regisseur', width=145, anchor=tk.CENTER)
        self.tree.column("Artist", width=175, anchor=tk.CENTER)
        # Присваиваем колонкам видимое название.
        self.tree.heading("ID", text="Номер")
        self.tree.heading("Film name", text="Название Фильма/Сериала")
        self.tree.heading("Year", text="Год")
        self.tree.heading("Genre", text="Жанр")
        self.tree.heading("Time", text="Время")
        self.tree.heading("Regisseur", text="Режиссер")
        self.tree.heading("Artist", text="Артисты в ролях")
        self.tree.pack()

    def records(self, film, year, genre, time, regisseur, artist):
        self.db.insert_data(film, year, genre, time, regisseur, artist)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM films''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):  # Вызов дочернего окна
        Child()


class Child(tk.Toplevel):  # Создадим дочернее окно для ввода данных в форму
    def __init__(self):  # Создаем конструктор класса
        super().__init__(root)  # Добавляем метод
        self.init_child()
        self.view = app

    def init_child(self):  # Добавляем объект и виджет дочернего окошка
        self.title("Добавь новый фильмец Бро!")  # Титутлка дочернего окна
        self.geometry('450x450+450+200')  # Типоразмеры
        self.resizable(False, False)  # Отключаем изменение размеров окна
        # Ввод данных в окне
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=160, y=30)
        self.entry_description = ttk.Entry(self)
        # self.entry_description.place(x=160, y=50)
        self.combobox = ttk.Combobox(self, values=[
            "1900",
            "1930",
            "1950",
            "1960",
            "1970",
            "1990",
            "2001",
            "2000",
            "2010",
            "2020",
            "2015"
        ])
        self.combobox.current(0)
        self.combobox.place(x=160, y=50)
        self.entry_description = ttk.Entry(self)
        # self.entry_description.place(x=160, y=70)
        self.combobox = ttk.Combobox(self, values=["Драма",
                                                   "Комедия",
                                                   "Экшен",
                                                   "Боевик",
                                                   "Исторический",
                                                   "Фантастика",
                                                   "Детский",
                                                   "Не Детский!"])
        self.combobox.current(0)
        self.combobox.place(x=160, y=70)
        self.entry_description = ttk.Entry(self)
        # self.entry_description.place(x=160, y=90)
        self.combobox = ttk.Combobox(self, values=(90,
                                                   120,
                                                   140,
                                                   180,
                                                   360))
        self.combobox.current(0)
        self.combobox.place(x=160, y=90)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=160, y=110)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=160, y=130)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=160, y=150)

        # Добавляем лейблы на дочернее окно
        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=30)
        label_description = tk.Label(self, text='Год выхода:')
        label_description.place(x=50, y=50)
        label_description = tk.Label(self, text='Жанр:')
        label_description.place(x=50, y=70)
        label_description = tk.Label(self, text='Длительность:')
        label_description.place(x=50, y=90)
        label_description = tk.Label(self, text='Режиссер:')
        label_description.place(x=50, y=110)
        label_description = tk.Label(self, text='В главных ролях:')
        label_description.place(x=50, y=130)
        label_description = tk.Label(self, text='Сюжет фильма:')
        label_description.place(x=50, y=150)

        # Добавляем кнопки управления
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)  # Кнопка выхода
        btn_cancel.place(x=290, y=210)  # Координаты Кнопки выхода

        btn_ok = ttk.Button(self, text='Добавить')  # Кнопка ввода-сохранения данных
        btn_ok.place(x=290, y=240)  # Координаты Кнопки ввода
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(), self.combobox.get(),))
                                                                  #self.regisseur.get(), #self.combobox.artist.get(),,)  # Реакция на кнопку мышки

        self.grab_set()
        self.focus_set()


# Создаем класс Базы Данных
class DB:
    def __init__(self):
        self.conn = sqlite3.connect("films.db")  # Создаем подключение к базе данных
        self.c = self.conn.cursor()  # Создаем курсор для взаимодействия с Базой
        self.c.execute('CREATE TABLE IF NOT EXISTS films(id integer primary key, film_mane text,\n'
                       'year integer, genre text, time integer, regisseur text, artist text)')
        self.conn.commit()

        # Добавляем данные в базу и таблицу и выводим на главное окно

    def insert_data(self, film, year, genre, time, regessier, artist):
        self.c.execute('''INSERT INTO film (film, year, genre, time, regisseur, artist) VALUES(!,!,!)''',
                       (film, year, genre, time, regisseur, artist)
                       )
        self.conn.commit()


if __name__ == '__main__':
    root = tk.Tk()  # Создадим корневое окно программы
    db = DB()  # Вызываем экземпляр класса DB
    app = Main(root)  # Будем создавать основное окно нашей программы
    app.pack()  # Упасковка содержимого методом pack
    root.title("Kinоmania")  # Названия нашей программы и его основное окно
    root.geometry("750x550+400+300")  # Зададим размер окна и расположение на экране
    root.resizable(False, False)  # Отключаем изменение размеров основного окна программы
    root.mainloop()  # Запуск приложения.
