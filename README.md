Телефонный справочник
-

Для сборки справочника в один файл необходимо выполнить:

>>> pyinstaller main.py --onefile -i phone.ico

Редактируем файл main.spec,
изменяем console=True на console=False для запуска
справочника без терминала. Выполняем:

>>> pyinstaller main.spec