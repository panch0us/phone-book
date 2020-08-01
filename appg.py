import tkinter
from tkinter import ttk

from tab_calculations import Appg
from tab_percent_positive import PercentPositive
from tab_percent import Percent
from tab_telephone import Telephone


class MainInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('УУР УМВД')
        self.window.geometry("1200x690")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5

        self.notebook = ttk.Notebook(self.window, width=1187, height=645)

        d_tab = Telephone(self.notebook)
        a_tab = Appg(self.notebook)
        #b_tab = PercentPositive(self.notebook)
        #c_tab = Percent(self.notebook)

        self.notebook.add(d_tab, text="  Телефонный справочник  ")
        self.notebook.add(a_tab, text="  АППГ  ")
        #self.notebook.add(b_tab, text="  Раскываемость  ")
        #self.notebook.add(c_tab, text="  АППГ от процента  ")


        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()