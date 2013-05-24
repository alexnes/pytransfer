Pytransfer
==========
Копирование файлов с удаленных компьютеров с помощью scp.
python + flask + scp.py
Установка (Debian)
-------------------
* ```aptitude install gcc python-dev python-pip python-virtualenv```
* В каталоге с программой:
```virtualenv venv```
```. venv/bin/activate```
```pip install flask paramiko```
Запуск
------
В каталоге с программой выполнить
```. venv/bin/activate```
```python index.py```
Настройка
---------
Настройки запуска задаются в файле index.py (строка ```app.run(debug=False, host='0.0.0.0', port=8088)```).

