Телефонный справочник

requirements:

altgraph==0.17 \
future==0.18.2 \
pefile==2019.4.18 \
pyinstaller==4.0 \
pyinstaller-hooks-contrib==2020.7 \
pywin32-ctypes==0.2.0

Для сборки справочника в один файл необходимо выполнить:
>>> pyinstaller main.py --onefile -i <имя иконки icon.ico>

Редактируем файл main.spec,
изменяем console=True на console=False для запуска
справочника без терминала.

>>> pyinstaller main.spec