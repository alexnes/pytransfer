Pytransfer
==========
����������� ������ � ��������� ����������� � ������� scp.
python + flask + scp.py
��������� (Debian)
-------------------
* ```aptitude install gcc python-dev python-pip python-virtualenv```
* � �������� � ����������:
```virtualenv venv```
```. venv/bin/activate```
```pip install flask paramiko```
������
------
� �������� � ���������� ���������
```. venv/bin/activate```
```python index.py```
���������
---------
��������� ������� �������� � ����� index.py (������ ```app.run(debug=False, host='0.0.0.0', port=8088)```).

