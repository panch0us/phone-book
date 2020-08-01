# ВЫЧИСЛЯЕМ АППГ

import tkinter
from tkinter import ttk

class Appg(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.frame_left = tkinter.LabelFrame(text='АППГ')
        self.frame_left.place(in_=self, x=5, y=5, height=600, width=390)

        self.frame_center = tkinter.LabelFrame(text='Проценты')
        self.frame_center.place(in_=self, x=396, y=5, height=600, width=390)

        self.frame_right = tkinter.LabelFrame(text='АППГ от процента')
        self.frame_right.place(in_=self, x=787, y=5, height=600, width=393)

        self.frame_bot = tkinter.LabelFrame()
        self.frame_bot.place(in_=self, x=5, y=605, height=33, width=1175)

        self.init_ui()

    def init_ui(self):
        """ Создаем виджет расчета АППГ для текущего окна"""
        ##### ЭЛЕМЕНТЫ ЛЕВОГО ОКНА - РАССЧЕТ АППГ #####
        # лейбл для отображения поля "текущий (анг. current) год"
        self.label_current_year_appg = tkinter.Label(self.frame_left, text='Введите значение текущего года: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.entry_current_year_appg = tkinter.Entry(self.frame_left, width=15)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_current_year_appg.place(x=8, y=10)
        self.entry_current_year_appg.place(x=220, y=10)

        ##### ЭЛЕМЕНТЫ ПРОШЛОГО ГОДА #####
        self.label_last_year_appg = tkinter.Label(self.frame_left, text='Введите значение прошлого года: ')
        self.entry_last_year_appg = tkinter.Entry(self.frame_left, width=15)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_last_year_appg.place(x=8, y=45)
        self.entry_last_year_appg.place(x=220, y=45)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        self.label_calculation_appg = tkinter.Label(self.frame_left, text='Результат: ')
        # StringVar - связан с элементом lable и в его поле textvariable вносит получившее значение
        # из переменной calculation.
        self.calculation_appg = tkinter.StringVar()
        self.label_calculation_result_appg = tkinter.Label(self.frame_left, textvariable=self.calculation_appg)
        # упаковываем созданные элементы (side - сторона).
        self.label_calculation_appg.place(x=8, y=138)
        self.label_calculation_result_appg.place(x=75, y=138)

        # линия после меню поиска в левом окне
        sep_search_appg = ttk.Separator(self.frame_left, orient="horizontal")
        sep_search_appg.place(x=0, y=180, relwidth=1.0)

        ##### КНОПКИ #####
        self.button_calculation_appg = tkinter.Button(self.frame_left, text='Рассчитать', command=self.calculation_appg)
        # упаковываем созданные элементы (side - сторона).
        self.button_calculation_appg.place(x=130, y=85)

        ##### ЭЛЕМЕНТЫ СРЕДНЕГО ОКНА - РАССЧЕТ ПРОЦЕНТОВ #####
        # лейбл для отображения поля "текущего (анг. current) год"
        self.label_current_year_percent = tkinter.Label(self.frame_center, text='Введите значение текущего года: ')
        # entry - (анг. вход) - поле для ввода данных пользователем
        self.entry_current_year_percent = tkinter.Entry(self.frame_center, width=10)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_current_year_percent.place(relx=0.1, rely=0.1)
        self.entry_current_year_percent.place(relx=0.7, rely=0.1)

        ##### ЭЛЕМЕНТЫ ПРОШЛОГО ГОДА #####
        self.label_last_year_percent = tkinter.Label(self.frame_center, text='Введите процент прошлого года: ')
        self.entry_last_year_percent = tkinter.Entry(self.frame_center, width=10)
        # устанавливаем расположение (place, анг. место) для элементов
        self.label_last_year_percent.place(relx=0.1, rely=0.2)
        self.entry_last_year_percent.place(relx=0.7, rely=0.2)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        self.label_calculation_percent = tkinter.Label(self.frame_center, text='Результат: ')
        # StringVar - связан с элементом lable и в его поле textvariable вносит получившее значение
        # из переменной calculation.
        self.calculation_percent = tkinter.StringVar()
        self.label_calculation_result_percent = tkinter.Label(self.frame_center, textvariable=self.calculation_percent)
        # упаковываем созданные элементы (side - сторона).
        self.label_calculation_percent.place(relx=0.1, rely=0.3)
        self.label_calculation_result_percent.place(relx=0.7, rely=0.3)

        ##### КНОПКИ #####
        self.button_calculation_percent = tkinter.Button(self.frame_center, text='Рассчитать', command=self.calculation_percent)

        # упаковываем созданные элементы (side - сторона).
        self.button_calculation_percent.place(relx=0.1, rely=0.4)


    def calculation_appg(self):
        # получаем данные из полей enty, куда пользоватеь ввоил свои данные, при помощи метода get
        self.current_year_appg = int(self.entry_current_year_appg.get())
        self.last_year_appg = int(self.entry_last_year_appg.get())
        # вычисляем АППГ
        self.calculation_result_appg = str(round(((self.current_year_appg - self.last_year_appg) / self.last_year_appg) * 100, 1)) + "%"
        # обновляем элемент label_calculation_result в рамке рачета, сохранив значение calculation_result в
        # объект StingVar, на который ссылается переменная calculation
        self.calculation_appg.set(self.calculation_result_appg)



    def calculation_percent(self):
        # получаем данные из полей enty, куда пользоватеь ввоил свои данные, при помощи метода get
        self.current_year_percent = int(self.entry_current_year_percent.get())
        self.last_year_percent = float(self.entry_last_year_percent.get())
        # вычисляем количество преступлений от процента, связанного с прошлым годом

        self.result_percent = 100 + self.last_year_percent
        self.result_sum_percent = self.current_year_percent * 100 / self.result_percent
        # разница
        self.difference_percent = self.current_year_percent - self.result_sum_percent
        self.appg_percent = round(self.current_year_percent - self.difference_percent)

        # обновляем элемент label_calculation_result в рамке рачета, сохранив значение calculation_result в
        # объект StingVar, на который ссылается переменная calculation
        self.calculation_percent.set(self.appg_percent)
