# ВЫЧИСЛЯЕМ АППГ

import tkinter
from tkinter import ttk

class Appg(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        # Создаем 3 фрейма (левый, центральный и правый)
        self.frame_left = tkinter.LabelFrame(text='АППГ')
        self.frame_left.place(in_=self, x=5, y=5, height=600, width=390)

        self.frame_center = tkinter.LabelFrame(text='Проценты')
        self.frame_center.place(in_=self, x=396, y=5, height=600, width=390)

        self.frame_right = tkinter.LabelFrame(text='АППГ от процента')
        self.frame_right.place(in_=self, x=787, y=5, height=600, width=393)

        self.frame_bot = tkinter.LabelFrame()
        self.frame_bot.place(in_=self, x=5, y=605, height=33, width=1175)

        # Создаем 3 функции для различных вычислений
        self.appg()
        self.percent()
        self.percent_appg()

    def appg(self):
        """Создаем элементы для расчета АППГ"""
        ##### ЭЛЕМЕНТЫ ТЕКУЩЕГО ГОДА #####
        label_current_year = tkinter.Label(self.frame_left, text='Введите значение текущего года: ')
        label_current_year.place(relx=0.1, rely=0.1)
        entry_current_year = tkinter.Entry(self.frame_left, width=10)
        entry_current_year.place(relx=0.7, rely=0.1)

        ##### ЭЛЕМЕНТЫ ПРОШЛОГО ГОДА #####
        label_last_year = tkinter.Label(self.frame_left, text='Введите значение прошлого года: ')
        label_last_year.place(relx=0.1, rely=0.2)
        entry_last_year = tkinter.Entry(self.frame_left, width=10)
        entry_last_year.place(relx=0.7, rely=0.2)

        ##### ЭЛЕМЕНТЫ РАСЧЕТА #####
        label_calculation = tkinter.Label(self.frame_left, text='Результат: ')
        label_calculation.place(relx=0.1, rely=0.3)
        self.calculation_appg = tkinter.StringVar()
        label_calculation_result = tkinter.Label(self.frame_left, textvariable=self.calculation_appg)
        label_calculation_result.place(relx=0.7, rely=0.3)

        ##### КНОПКИ #####
        button_calculation = tkinter.Button(self.frame_left, text='Рассчитать', command=self.calculation_def)
        button_calculation.place(relx=0.1, rely=0.4)

        return entry_current_year.get(), entry_last_year.get()


    def percent(self):
        pass

    def percent_appg(self):
        pass



    def calculation_def(self):
        pass
