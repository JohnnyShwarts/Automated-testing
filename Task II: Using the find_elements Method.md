## Задание


![Scree_1](https://user-images.githubusercontent.com/104720406/181619860-cb01db2b-80e2-4107-98ca-4e5dd6ae359a.png)


[**Cсылка на форму для заполнения**](http://suninjuly.github.io/huge_form.html)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    funnyWords = ["milk", "pizza", "poncho", "pasta", "ice_cream", "hotdog", "popcorn", "jello", "chicken", "pie", "eggs", "pudding", "kebab", "fish", "wetFish", "tuna", "calamary"]
    for element in elements:
     element.send_keys(random.choice(funnyWords))



    # for element in elements:
    #     element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
```
