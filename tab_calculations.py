# ВЫЧИСЛЯЕМ АППГ

import tkinter
from tkinter import ttk

class Appg(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        # Создаем 3 фрейма (левый, центральный и правый)
        self.frame_left = tkinter.LabelFrame(text='АППГ')
        self.frame_left.place(in_=self, x=5, y=5, height=614, width=390)

        self.frame_center = tkinter.LabelFrame(text='Проценты')
        self.frame_center.place(in_=self, x=396, y=5, height=614, width=390)

        self.frame_right = tkinter.LabelFrame(text='Раскрываемость')
        self.frame_right.place(in_=self, x=787, y=5, height=614, width=393)

        self.frame_bot = tkinter.LabelFrame()
        self.frame_bot.place(in_=self, x=5, y=623, height=30, width=1175)

        # Инициируем запуск 3 функций для различных вычислений
        self.appg()
        self.percent()
        self.percent_appg()

        # ЛЕЙБЛ АВТОРА
        label_author = tkinter.Label(self.frame_bot, text='© Савкин П.В. 2020')
        # entry - (анг. вход) - поле для ввода данных пользователем
        label_author.place(x=1050, y=3)

    def appg(self):
        """Создаем элементы для расчета АППГ"""
        ##### ЭЛЕМЕНТЫ ТЕКУЩЕГО ГОДА #####
        label_current_year = tkinter.Label(self.frame_left, text='Введите значение текущего года: ')
        label_current_year.place(relx=0.1, rely=0.1)
        self.appg_entry_current_year = tkinter.Entry(self.frame_left, width=10)
        self.appg_entry_current_year.place(relx=0.7, rely=0.1)

        ##### ЭЛЕМЕНТЫ ПРОШЛОГО ГОДА #####
        label_last_year = tkinter.Label(self.frame_left, text='Введите значение прошлого года: ')
        label_last_year.place(relx=0.1, rely=0.2)
        self.appg_entry_last_year = tkinter.Entry(self.frame_left, width=10)
        self.appg_entry_last_year.place(relx=0.7, rely=0.2)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        label_calculation = tkinter.Label(self.frame_left, text='Результат: ')
        label_calculation.place(relx=0.1, rely=0.3)
        self.calculation_count_appg = tkinter.StringVar()
        label_calculation_result = tkinter.Label(self.frame_left, textvariable=self.calculation_count_appg)
        label_calculation_result.place(relx=0.7, rely=0.3)

        ##### КНОПКИ #####
        button_calculation_appg = tkinter.Button(self.frame_left, text='Рассчитать', command=self.calculation_appg)
        button_calculation_appg.place(relx=0.1, rely=0.4)

    def percent(self):
        """Создаем элементы для расчета процентов"""
        ##### ЭЛЕМЕНТЫ ТЕКУЩЕГО ГОДА #####
        label_current_year = tkinter.Label(self.frame_center, text='Введите значение текущего года: ')
        label_current_year.place(relx=0.1, rely=0.1)
        self.percent_entry_current_year = tkinter.Entry(self.frame_center, width=10)
        self.percent_entry_current_year.place(relx=0.7, rely=0.1)

        ##### ЭЛЕМЕНТЫ ПРОШЛОГО ГОДА #####
        label_last_year_percent = tkinter.Label(self.frame_center, text='Введите процент прошлого года: ')
        label_last_year_percent.place(relx=0.1, rely=0.2)
        self.percent_entry_last_year_percent = tkinter.Entry(self.frame_center, width=10)
        self.percent_entry_last_year_percent.place(relx=0.7, rely=0.2)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        label_calculation = tkinter.Label(self.frame_center, text='Результат: ')
        label_calculation.place(relx=0.1, rely=0.3)
        self.calculation_count_percent = tkinter.StringVar()
        label_calculation_result = tkinter.Label(self.frame_center, textvariable=self.calculation_count_percent)
        label_calculation_result.place(relx=0.7, rely=0.3)

        ##### КНОПКИ #####
        button_calculation = tkinter.Button(self.frame_center, text='Рассчитать', command=self.calculation_percent)
        button_calculation.place(relx=0.1, rely=0.4)

    def percent_appg(self):
        """Создаем элементы для расчета раскрываемости"""
        ##### РАСКРЫТЫЕ ПРЕСТУПЛЕНИЯ #####
        # лейбл для отображения поля "Раскрыто" (анг. crime_solved - раскрыто преступление)
        label_crime_solved = tkinter.Label(self.frame_right, text='Введите количество раскрытых преступлений: ')
        label_crime_solved.place(relx=0.05, rely=0.1)
        self.entry_crime_solved = tkinter.Entry(self.frame_right, width=7)
        self.entry_crime_solved.place(relx=0.85, rely=0.1)

        ##### ПРИОСТАНОВЛЕННЫЕ ПРЕСТУПЛЕНИЯ #####
        # (анг. suspended_crime - приостановлено преступление)
        label_suspended_crime = tkinter.Label(self.frame_right, text='Введите количество приостановленных преступлений: ')
        label_suspended_crime.place(relx=0.05, rely=0.2)
        self.entry_suspended_crime = tkinter.Entry(self.frame_right, width=7)
        self.entry_suspended_crime.place(relx=0.85, rely=0.2)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        label_calculation = tkinter.Label(self.frame_right, text='Результат: ')
        label_calculation.place(relx=0.05, rely=0.3)
        # StringVar - связан с элементом lable и в его поле textvariable вносит получившее значение
        # из переменной calculation.
        self.calculation_count_percent_and_appg = tkinter.StringVar()
        label_calculation_result = tkinter.Label(self.frame_right, textvariable=self.calculation_count_percent_and_appg)
        label_calculation_result.place(relx=0.85, rely=0.3)

        ##### КНОПКИ #####
        button_calculation = tkinter.Button(
            self.frame_right, text='Рассчитать', command=self.calculation_percent_appg)
        button_calculation.place(relx=0.05, rely=0.4)

    def calculation_appg(self):
        current_year = int(self.appg_entry_current_year.get())
        last_year = int(self.appg_entry_last_year.get())
        # вычисляем АППГ
        calculation_result = str(round(((current_year - last_year) / last_year) * 100, 1)) + "%"
        # обновляем элемент label_calculation_result в рамке рачета, сохранив значение calculation_result в
        # объект StingVar, на который ссылается переменная calculation
        self.calculation_count_appg.set(calculation_result)

    def calculation_percent(self):
        current_year = int(self.percent_entry_current_year.get())
        last_year_persent = float(self.percent_entry_last_year_percent.get())
        # вычисляем количество преступлений от процента, связанного с прошлым годом
        result_persent = 100 + last_year_persent
        result_sum = current_year * 100 / result_persent
        # разница
        difference = current_year - result_sum
        appg = round(current_year - difference)
        # обновляем элемент label_calculation_result в рамке рачета, сохранив значение calculation_result в
        # объект StingVar, на который ссылается переменная calculation
        self.calculation_count_percent.set(appg)

    def calculation_percent_appg(self):
        # получаем данные из полей enty, куда пользоватеь ввоил свои данные, при помощи метода get
        quantity_crime_solved = int(self.entry_crime_solved.get())
        quantity_suspended_crime = int(self.entry_suspended_crime.get())
        # вычисляем АППГ
        calculation_result = str(round(
            quantity_crime_solved / (quantity_crime_solved + quantity_suspended_crime) * 100, 1)) + "%"
        # обновляем элемент label_calculation_result в рамке рачета, сохранив значение calculation_result в
        # объект StingVar, на который ссылается переменная calculation
        self.calculation_count_percent_and_appg.set(calculation_result)