# Automated-testing
___```Selenium+Python```___

## Installing Python on Windows

Для начала скачиваем установочный файл для Python с [официального сайта](https://www.python.org/downloads/windows/), выбераем стабильную версию для Windows в зависимости от вашей зистемы (64-разрядная или 32-разрядная)

В окне установки пакета ставим галочку в разделе __Add Python... to PATH__ ( Это даст возможность вызовать интерпретатор Python из командной строки)

## Запуск командной строки
Для запуска командной строки воспользуйтесь одним из следующих способов:

* Пуск → Выполнить» (или клавиши Win+R) введите cmd и нажмите клавишу Enter;
* Пуск → Все программы → Стандартные → Командная строка»;
* Пуск → Поиск → Командная строка».
[Полная ссылка тут ->>>](https://cmd.readthedocs.io/cmd.html)

После установки пакета Python, В консоли введите python --version (на некоторых сборках Windows нужно вводить короткую команду, например, py --version)
:![py_vers_1](https://user-images.githubusercontent.com/104720406/176993136-3e703fe4-0cac-4de4-ac63-c2a5b556e079.png)

## Создаем виртуальное окружение для Python
(Чтобы не засорять наше основное Python-окружение)

* Создадим папку, где будут храниться наши виртуальные окружения, и перейдем в неё

```mkdir environments```
```cd environments```

* Создадим виртуальное окружение:

```python -m venv selenium_env```
* Запустим созданный для нас приложением venv файл activate.bat, чтобы активировать окружение:

```selenium_env\Scripts\activate.bat```

a) Если все прошло удачно, в скобках появится такой тескт **<selenium_env>**
![env_1](https://user-images.githubusercontent.com/104720406/176995400-9b1871c2-5ec7-41e7-9c01-775cf6e895e7.png)

b) Для выхода из окружения достаточно выполнить команду **deactivate**
![deactivate_1](https://user-images.githubusercontent.com/104720406/176995492-76877a60-6eac-4489-a2c2-6169d9784fe4.png)

c) Запустим интерпретатор Python и напишем __HelloWorld__:
> ```selenium_env\Scripts\activate.bat```
>> ```Python```
>>> ```print("Hello, World!")```

![hW_1](https://user-images.githubusercontent.com/104720406/176995825-716ead1e-37fc-4d76-9d02-af3890798585.png)

d) Выйдем из интерпретатора:

> ```exit()```
