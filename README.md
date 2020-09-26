Телефонный справочник
-

Для сборки справочника в один файл необходимо выполнить:
>>> pyinstaller main.py --onefile -i <имя иконки icon.ico>

Редактируем файл main.spec,
изменяем console=True на console=False для запуска
справочника без терминала.

>>> pyinstaller main.spec