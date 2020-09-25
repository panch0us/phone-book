# ТЕЛЕФОННЫЙ СПРАВОЧНИК
"""
Описание
"""

import tkinter
from tkinter import ttk
from tkinter.font import Font
import sqlite3
import os.path

# создаем глобальную переменную для запоминания выбранного поля поиска (имя или телефон или работа и т.п.)
FUNCTION_VALUE = ''
# создаем глобальную переменную для запоминания сожержания SQL запроса
SQL_VALUE = ''

class Telephone(tkinter.Frame):
    """Телефонный справочник"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # Задаем стандартный шрифт и размер шрифта для приложения
        self.myFont = Font(family="Courier", size=10)

        self.frame_left = tkinter.LabelFrame()
        self.frame_left.place(in_=self, x=5, y=5, height=614, width=650)

        self.frame_right = tkinter.LabelFrame()
        self.frame_right.place(in_=self, x=660, y=5, height=614, width=520)

        self.frame_bot = tkinter.LabelFrame()
        self.frame_bot.place(in_=self, x=5, y=623, height=30, width=1175)

        self.exist_database()
        self.init_ui(self.select_all_from_database())

    def exist_database(self):
        """Проверка существования базы данных или создание базы данных"""
        self.file_path = 'mydatabase.db'

        if not os.path.exists(self.file_path):
            conn = sqlite3.connect("mydatabase.db")
            cursor = conn.cursor()

            # Создание таблицы c 6 полями (1 - id с автоинкрементом, 2 - имя, 3 - телефон, 4 - район,
            # 5 - место работы, 6 - должность, 7 - разное)
            cursor.execute("""CREATE TABLE phone_book
                            (id INTEGER PRIMARY KEY,
                              name text,
                              phone text,
                              area text,
                              workplace text,
                              position text,
                              other text)""")
            conn.close()
        else:
            print('База данных уже создана')

    def select_all_from_database(self):
        """ Выбираем всю информацию из таблицы phone_book БД"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        sql = "SELECT * FROM phone_book"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_name_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE name LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_phone_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску номера телефона"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE phone LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_area_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE area LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_workplace_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску места работы"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE workplace LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_position_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску должности"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE position LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def select_other_from_database(self, sql_value):
        """ Выбираем информацию из таблицы phone_book БД, путем фильтра по поиску позиции иное"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE other LIKE '%{sql_value}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    def update_from_database(self):
        """ Обновляем информацию о контакте """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        if self.update_id.get():
            if self.update_name.get():
                sql = f"UPDATE phone_book SET name = '{str(self.update_name.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                # если удаляем символы из поля, то сохраняется пустая строка
                sql = f"UPDATE phone_book SET name = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            if self.update_phone.get():
                sql = f"UPDATE phone_book SET phone = '{str(self.update_phone.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                sql = f"UPDATE phone_book SET phone = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            if self.update_area.get():
                sql = f"UPDATE phone_book SET area = '{str(self.update_area.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                sql = f"UPDATE phone_book SET area = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            if self.update_workplace.get():
                sql = f"UPDATE phone_book SET workplace = '{str(self.update_workplace.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                sql = f"UPDATE phone_book SET workplace = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            if self.update_position.get():
                sql = f"UPDATE phone_book SET position = '{str(self.update_position.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                sql = f"UPDATE phone_book SET position = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            if self.update_other.get():
                sql = f"UPDATE phone_book SET other = '{str(self.update_other.get()).lower()}' " \
                      f"WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
            else:
                sql = f"UPDATE phone_book SET other = '' WHERE id = {self.update_id.get()}"
                cursor.execute(sql)
        conn.commit()
        conn.close()
        self.text.destroy()
        self.scroll.destroy()
        # повторно вызываем функцию по созданию элементов text и scroll

        self.current_status_search()

        self.new_window_update_contact.destroy()

    def init_ui(self, func):
        """Создание телефонной книги"""
        self.text = tkinter.Text(self.frame_left, width=77, height=37)
        for i in func:
            self.text.insert(tkinter.INSERT, f'ID:\t|{i[0]}\n'
                                             f'ФИО:\t|{str(i[1]).title()}\n'
                                             f'ТЕЛ:\t|{str(i[2]).title()}\n'
                                             f'РАЙОН:\t|{str(i[3]).title()}\n'
                                             f'РАБОТА:\t|{str(i[4]).title()}\n'
                                             f'ДОЛЖН:\t|{str(i[5]).title()}\n'
                                             f'РАЗНОЕ:\t|{str(i[6]).title()}\n' + ('-' * 76) + '\n')
        self.text.configure(state='disabled', font=self.myFont)

        # создаем "скроллер" (ползунок прокрутки), который устанавливается comand=text.yview, где y - ось.
        self.scroll = tkinter.Scrollbar(self.frame_left, command=self.text.yview)
        # RIGHT - ползунок справа, Y - по оси Y.
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # расположение элемента <TEXT>, например side=tkinter.LEFT
        self.text.place(x=5, y=5)
        self.text.config(yscrollcommand=self.scroll.set)

        ##### МЕНЮ ПОИСКА ПО ФИО #####
        self.label_search = tkinter.Label(self.frame_right, text='Поиск по имени: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_contact = tkinter.StringVar()
        self.entry_search = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_contact)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search.place(x=5, y=10)
        self.entry_search.place(x=160, y=10)

        ##### МЕНЮ ПОИСКА ПО НОМЕРУ ТЕЛЕФОНА #####
        self.label_search_phone = tkinter.Label(self.frame_right, text='Поиск по телефону: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_phone = tkinter.StringVar()
        self.entry_search_phone = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_phone)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search_phone.place(x=5, y=40)
        self.entry_search_phone.place(x=160, y=40)

        ##### МЕНЮ ПОИСКА ПО РАЙОНУ #####
        self.label_search_area = tkinter.Label(self.frame_right, text='Поиск по району: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_area = tkinter.StringVar()
        self.entry_search_area = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_area)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search_area.place(x=5, y=70)
        self.entry_search_area.place(x=160, y=70)

        ##### МЕНЮ ПОИСКА ПО РАБОТЕ #####
        self.label_search_workplace = tkinter.Label(self.frame_right, text='Поиск по работе: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_workplace = tkinter.StringVar()
        self.entry_search_workplace = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_workplace)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search_workplace.place(x=5, y=100)
        self.entry_search_workplace.place(x=160, y=100)

        ##### МЕНЮ ПОИСКА ПО ДОЛЖНОСТИ #####
        self.label_search_position = tkinter.Label(self.frame_right, text='Поиск по должности: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_position = tkinter.StringVar()
        self.entry_search_position = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_position)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search_position.place(x=5, y=130)
        self.entry_search_position.place(x=160, y=130)

        ##### МЕНЮ ПОИСКА ПО ПОЗИЦИИ РАЗНОЕ #####
        self.label_search_other = tkinter.Label(self.frame_right, text='Поиск по пункту разное: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.search_other = tkinter.StringVar()
        self.entry_search_other = tkinter.Entry(self.frame_right, width=32, textvariable=self.search_other)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_search_other.place(x=5, y=160)
        self.entry_search_other.place(x=160, y=160)

        ##### КНОПКИ #####
        # Кнопка поиска по ФИО
        self.button_search = tkinter.Button(self.frame_right, text='Найти', command=self.search_def_name_restart)
        self.button_search.place(x=370, y=10, height=20)
        # Кнопка поиска по номеру телефона
        self.button_search_phone = tkinter.Button(self.frame_right, text='Найти', command=self.search_def_phone_restart)
        self.button_search_phone.place(x=370, y=40, height=20)
        # Кнопка поиска по району
        self.button_search_area = tkinter.Button(self.frame_right, text='Найти', command=self.search_def_area_restart)
        self.button_search_area.place(x=370, y=70, height=20)
        # Кнопка поиска по месту работы
        self.button_search_workplace = tkinter.Button(self.frame_right, text='Найти',
                                                      command=self.search_def_workplace_restart)
        self.button_search_workplace.place(x=370, y=100, height=20)
        # Кнопка поиска по должности
        self.button_search_position = tkinter.Button(self.frame_right, text='Найти',
                                                      command=self.search_def_position_restart)
        self.button_search_position.place(x=370, y=130, height=20)
        # Кнопка поиска по позиции иное
        self.button_search_other = tkinter.Button(self.frame_right, text='Найти',
                                                     command=self.search_def_other_restart)
        self.button_search_other.place(x=370, y=160, height=20)

        # кнопка очистки поиска (для возврата стандартного значения)
        self.button_search_all = tkinter.Button(
            self.frame_right, text='Сброс\nпараметров\nпоиска', command=self.default_result)
        self.button_search_all.place(x=428, y=71, height=48)
        # Кнопка вызова нового окна для добавления контакта
        self.add_new_window = tkinter.Button(
            self.frame_right, text='   Добавить   ', command=self.create_new_window_add_member)
        self.add_new_window.place(x=80, y=230)
        # кнопка возова нового окна для удаления контакта
        self.delete_member_button = tkinter.Button(
            self.frame_right, text='   Удалить   ', command=self.create_new_window_delete_member)
        self.delete_member_button.place(x=220, y=230)
        # кнопка для изменения контакта
        self.update_member_button = tkinter.Button(
            self.frame_right, text='  Изменить  ', command=self.create_new_window_update_member_1)
        self.update_member_button.place(x=350, y=230)

        # РАЗДЕЛИТЕЛЬНЫЕ ЛИНИИ
        # линия после меню поиска в правом окне
        sep_search = ttk.Separator(self.frame_right, orient="horizontal")
        sep_search.place(x=0, y=195, relwidth=1.0)

        # линия после меню изменения контактов в правом окне
        sep_menu_contact = ttk.Separator(self.frame_right, orient="horizontal")
        sep_menu_contact.place(x=0, y=285, relwidth=1.0)

        # ЛЕЙБЛ МЕНЮ КОНТАКТОВ
        self.label_menu_contact = tkinter.Label(self.frame_right, text='Меню управления контактами')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.label_menu_contact.place(x=170, y=200)

        # ЛЕЙБЛ АВТОРА
        self.label_author = tkinter.Label(self.frame_bot, text='© Савкин П.В. 2020, ver. 1.1')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.label_author.place(x=1000, y=3)

    def create_new_window_delete_member(self):
        """Открывается новое окно для удаления контакта"""
        self.new_window_delete_member = tkinter.Toplevel()
        self.new_window_delete_member.geometry("280x120")
        self.new_window_delete_member.title('Удаление контакта')
        self.new_window_delete_member.resizable(width=False, height=False)
        # в переменную self.id получаем данные их поля entry_add_area, опции textvariable
        self.id = tkinter.StringVar()
        label_add_area = tkinter.Label(self.new_window_delete_member, text='Введите ID для удаления контакта: ')
        entry_add_area = tkinter.Entry(self.new_window_delete_member, width=5, textvariable=self.id)
        label_add_area.place(x=5, y=10)
        entry_add_area.place(x=210, y=10)

        ##### КНОПКИ #####
        # кнопка добавления ногого контакта
        button_delete_member = tkinter.Button(self.new_window_delete_member, text='Удалить',
                                              command=self.delete_member_from_db)
        button_delete_member.place(x=110, y=80)

        self.new_window_delete_member.mainloop()

    def delete_member_from_db(self):
        """ Удаляем контакт из БД """
        # присваиваем id значение, введенное из переменной self.id функции create_new_window_delete_member
        id = self.id.get()
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM phone_book WHERE id = ?""", (id,))
        conn.commit()
        conn.close()
        # уничтожаем в главном окне элемент text и элемент scroll
        self.text.destroy()
        self.scroll.destroy()

        # Вызываем функцию, которая проверяет в каком окне поиска находится пользователь в настоящий момент.
        # В результате при добавлении, удалении или изменении контакта, пользователь остается в томже окне,
        # но только с обновленными данными.
        self.current_status_search()
        # уничтожаем второстепенное окно
        self.new_window_delete_member.destroy()

    def create_new_window_add_member(self):
        """Выполняется при нажатии кнопки "Добавить" """
        self.new_window = tkinter.Toplevel()
        self.new_window.geometry("600x250")
        self.new_window.title('Окно для добавления нового контакта')
        self.new_window.resizable(width=False, height=False)

        self.name = tkinter.StringVar()
        label_add_name = tkinter.Label(self.new_window, text='Введите ФИО: ')
        entry_add_name = tkinter.Entry(self.new_window, width=55, textvariable=self.name)
        label_add_name.place(x=5, y=10)
        entry_add_name.place(x=250, y=10)

        self.phone = tkinter.StringVar()
        label_add_phone = tkinter.Label(self.new_window, text='Введите номер телефона: ')
        entry_add_phone = tkinter.Entry(self.new_window, width=55, textvariable=self.phone)
        label_add_phone.place(x=5, y=40)
        entry_add_phone.place(x=250, y=40)

        self.area = tkinter.StringVar()
        label_add_area = tkinter.Label(self.new_window, text='Введите район: ')
        entry_add_area = tkinter.Entry(self.new_window, width=55, textvariable=self.area)
        label_add_area.place(x=5, y=70)
        entry_add_area.place(x=250, y=70)

        self.workplace = tkinter.StringVar()
        label_add_workplace = tkinter.Label(self.new_window, text='Введите место работы: ')
        entry_add_workplace = tkinter.Entry(self.new_window, width=55, textvariable=self.workplace)
        label_add_workplace.place(x=5, y=100)
        entry_add_workplace.place(x=250, y=100)

        self.position = tkinter.StringVar()
        label_add_position = tkinter.Label(self.new_window, text='Введите должность или описание: ')
        entry_add_position = tkinter.Entry(self.new_window, width=55, textvariable=self.position)
        label_add_position.place(x=5, y=130)
        entry_add_position.place(x=250, y=130)

        self.other = tkinter.StringVar()
        label_add_other = tkinter.Label(self.new_window, text='Введите заметки: ')
        entry_add_other = tkinter.Entry(self.new_window, width=55, textvariable=self.other)
        label_add_other.place(x=5, y=160)
        entry_add_other.place(x=250, y=160)

        ##### КНОПКИ #####
        button_add_member = tkinter.Button(self.new_window, text='Добавить', command=self.insert_to_database)
        button_add_member.place(x=250, y=210)

        self.new_window.mainloop()

    def insert_to_database(self):
        """Вносим новых членов телефонной книги"""
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        name = self.name.get().lower()
        phone = self.phone.get().lower()
        area = self.area.get().lower()
        workplace = self.workplace.get().lower()
        position = self.position.get().lower()
        other = self.other.get().lower()

        member = [(name, phone, area, workplace, position, other)]

        cursor.executemany(
            "INSERT INTO phone_book(name, phone, area, workplace, position, other) VALUES (?,?,?,?,?,?)", member)
        # Сохраняем изменения
        conn.commit()
        conn.close()

        self.text.destroy()
        self.scroll.destroy()

        # Добавить описание
        self.current_status_search()

        self.new_window.destroy()

    def create_new_window_update_member_1(self):
        """ "ИЗМЕНИТЬ № 1" Создает окно, выполняется при нажатии кнопки "ИЗМЕНИТЬ" """
        self.new_window_update_member_1 = tkinter.Toplevel()
        self.new_window_update_member_1.geometry("285x120")
        self.new_window_update_member_1.title('Изменение контакта')
        self.new_window_update_member_1.resizable(width=False, height=False)
        # в переменную self.id получаем данные их поля entry_add_area, опции textvariable
        self.update_id = tkinter.StringVar()
        label_add_area = tkinter.Label(self.new_window_update_member_1, text='Введите ID для изменения контакта: ')
        entry_add_area = tkinter.Entry(self.new_window_update_member_1, width=5, textvariable=self.update_id)
        label_add_area.place(x=5, y=10)
        entry_add_area.place(x=210, y=10)

        ##### КНОПКИ #####
        # кнопка изменения контакта
        button_update_member_1 = tkinter.Button(self.new_window_update_member_1, text='Изменить',
                                              command=self.create_new_window_update_member_2)
        button_update_member_1.place(x=110, y=80)

        self.new_window_update_member_1.mainloop()

    def create_new_window_update_member_2(self):
        """Выполняется после выбора ID в первой кнопке ИЗМЕНИТЬ"""
        # уничтожаем первое окно ИЗМЕНИТЬ
        self.new_window_update_member_1.destroy()

        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        # применяем к полученному результаты функции self.search_contact.get() метод строки - .lower()
        # для перевода всей строки к нижнему регистру
        sql = f"SELECT * FROM phone_book WHERE id = '{self.update_id.get()}'"
        cursor.execute(sql)
        # получаем строки из таблицы phone_book, где id = id из окна "ИЗМЕНИТЬ № 1"
        result = cursor.fetchall()
        conn.close()

        for i in result:
            self.entry_name = i[1]
            self.entry_phone = i[2]
            self.entry_area = i[3]
            self.entry_workplace = i[4]
            self.entry_position = i[5]
            self.entry_other = i[6]

        self.new_window_update_contact = tkinter.Toplevel()
        self.new_window_update_contact.geometry("600x230")
        self.new_window_update_contact.title('Окно для изменения контакта')
        self.new_window_update_contact.resizable(width=False, height=False)


        self.update_name = tkinter.StringVar()
        label_update_name = tkinter.Label(self.new_window_update_contact, text='Измените ФИО: ')
        entry_update_name = tkinter.Entry(self.new_window_update_contact, width=55, textvariable=self.update_name)
        entry_update_name.insert(0, str(self.entry_name).title())
        label_update_name.place(x=5, y=10)
        entry_update_name.place(x=250, y=10)

        self.update_phone = tkinter.StringVar()
        label_update_phone = tkinter.Label(self.new_window_update_contact, text='Измените номер телефона: ')
        entry_update_phone = tkinter.Entry(self.new_window_update_contact, width=55, textvariable=self.update_phone)
        entry_update_phone.insert(0, self.entry_phone)
        label_update_phone.place(x=5, y=40)
        entry_update_phone.place(x=250, y=40)

        self.update_area = tkinter.StringVar()
        label_update_area = tkinter.Label(self.new_window_update_contact, text='Измените район: ')
        entry_update_area = tkinter.Entry(self.new_window_update_contact, width=55, textvariable=self.update_area)
        entry_update_area.insert(0, str(self.entry_area).title())
        label_update_area.place(x=5, y=70)
        entry_update_area.place(x=250, y=70)

        self.update_workplace = tkinter.StringVar()
        label_update_workplace = tkinter.Label(self.new_window_update_contact, text='Измените место работы: ')
        entry_update_workplace = tkinter.Entry(self.new_window_update_contact, width=55,
                                               textvariable=self.update_workplace)
        entry_update_workplace.insert(0, str(self.entry_workplace).title())
        label_update_workplace.place(x=5, y=100)
        entry_update_workplace.place(x=250, y=100)

        self.update_position = tkinter.StringVar()
        label_update_position = tkinter.Label(self.new_window_update_contact, text='Измените должность или описание: ')
        entry_update_position = tkinter.Entry(self.new_window_update_contact, width=55,
                                              textvariable=self.update_position)
        entry_update_position.insert(0, str(self.entry_position).title())
        label_update_position.place(x=5, y=130)
        entry_update_position.place(x=250, y=130)

        self.update_other = tkinter.StringVar()
        label_update_other = tkinter.Label(self.new_window_update_contact, text='Измените описание позиции разное: ')
        entry_update_other = tkinter.Entry(self.new_window_update_contact, width=55,
                                              textvariable=self.update_other)
        entry_update_other.insert(0, str(self.entry_other).title())
        label_update_other.place(x=5, y=160)
        entry_update_other.place(x=250, y=160)

        ##### КНОПКИ #####
        button_add_member = tkinter.Button(self.new_window_update_contact, text='Изменить',
                                           command=self.update_from_database)
        button_add_member.place(x=250, y=200)

        self.new_window_update_contact.mainloop()

    def search_def_name_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'name'
        SQL_VALUE = str(self.search_contact.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_name_from_database(SQL_VALUE))

    def search_def_phone_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'phone'
        SQL_VALUE = str(self.search_phone.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_phone_from_database(SQL_VALUE))

    def search_def_area_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'area'
        SQL_VALUE = str(self.search_area.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_area_from_database(SQL_VALUE))

    def search_def_workplace_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'workplace'
        SQL_VALUE = str(self.search_workplace.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_workplace_from_database(SQL_VALUE))

    def search_def_position_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'position'
        SQL_VALUE = str(self.search_position.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_position_from_database(SQL_VALUE))

    def search_def_other_restart(self):
        global FUNCTION_VALUE
        global SQL_VALUE
        FUNCTION_VALUE = 'other'
        SQL_VALUE = str(self.search_other.get().lower())
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_other_from_database(SQL_VALUE))

    def default_result(self):
        """Передает в функцию unit_ui функцию select_all_from_database
        для вывода всех элементов из таблицы phone_book на элемент tkinter.Text"""
        self.text.destroy()
        self.scroll.destroy()
        self.init_ui(self.select_all_from_database())

    def current_status_search(self):
        """Функция проверяет в каком окне поиска находится пользователь в настоящий момент.
        В результате при добавлении, удалении или изменении контакта, пользователь остается в томже окне,
        но только с обновленными данными.
        FUNCTION_VALUE - Глобальная переменная используется для проверки позиции: в каком окне поиска находится
        пользователь и на основе выбора отправляет нужный sql запрос через необходимую функцию.
        SQL_VALUE - sql-код получаем из глобальной переменной SQL_VALUE"""
        global FUNCTION_VALUE

        if FUNCTION_VALUE == 'name':
            self.init_ui(self.select_name_from_database(SQL_VALUE))
        elif FUNCTION_VALUE == 'phone':
            self.init_ui(self.select_phone_from_database(SQL_VALUE))
        elif FUNCTION_VALUE == 'area':
            self.init_ui(self.select_area_from_database(SQL_VALUE))
        elif FUNCTION_VALUE == 'workplace':
            self.init_ui(self.select_workplace_from_database(SQL_VALUE))
        elif FUNCTION_VALUE == 'position':
            self.init_ui(self.select_position_from_database(SQL_VALUE))
        elif FUNCTION_VALUE == 'other':
            self.init_ui(self.select_other_from_database(SQL_VALUE))
        else:
            self.init_ui(self.select_all_from_database())