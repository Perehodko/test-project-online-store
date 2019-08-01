# test-project-online-store

Тесты написаны с использование шаблона Page Object

Работаю с драйвером для Chrome.

Тестирование организованно с помощью:

- Python 3.7.3
- Система управления пакетами pip
- Бибилиотека Selenium 3.13.0
- Драйвер для Chrome ChromeDriver
- unittest
- PyTest 3.10.1

Linux

Установка системы управления пакетами pip:
```
$ sudo apt-get install -y python3-pip
```
Установка библиотеки Selenium:
```
pip install selenium==3.13.0
pip list
```
Установка ChromeDriver:
```
$ wget https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
```
Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver
```
Установка PyTest:
```
$ pip install pytest==3.10.1
```

Для запуска тестов используйте команду:
```
pytest -s test_main_page.py
pytest -s test_product_page.py
```
