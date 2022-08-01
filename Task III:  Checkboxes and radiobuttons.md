## Checkboxes и radiobuttons (капча для роботов)

### Задание


Программа должна выполнить следующие шаги:

- Открыть страницу [https://suninjuly.github.io/math.html](https://suninjuly.github.io/math.html)

- Считать значение для переменной x.
- Посчитать математическую функцию от x (код для этого приведён ниже).
- Ввести ответ в текстовое поле.
- Отметить checkbox "I'm the robot".
- Выбрать radiobutton "Robots rule!".
- Нажать на кнопку Submit.

__Для этой задачи вам понадобится использовать атрибут ```.text``` для найденного элемента. Обратите внимание, что скобки здесь не нужны:__

```python
x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)
```
_Атрибут ```text``` возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
Например, text для данного элемента ```<div class="message"> У вас новое сообщение.</div>``` вернёт строку: "У вас новое сообщение"._

_Используйте функцию ```calc()```, которая рассчитает и вернет вам значение функции, 
которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта:_

```python
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
```


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x = browser.find_element(By.ID, "input_value").text
y = calc(x)

link = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]').send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
option2.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
```

## Задание выполнено
![Screenshot_1](https://user-images.githubusercontent.com/104720406/182222166-1e967c2e-a8d1-442e-a803-bf73da5c059b.png)
