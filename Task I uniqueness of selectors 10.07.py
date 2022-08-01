# task 10.07

# Uniqueness of Selectors

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Your code that fills in the required fields
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("Johnny")
    
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys("Shwarts")
   
    input3 = browser.find_element(By.CLASS_NAME, "third").send_keys("gogo@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys(4402215)

    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys("India")


    # Submitting the completed form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Check if you can register
    # waiting for the page to load
    time.sleep(5)

    # find element containing text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # write the text from the welcome_text_elt element to the welcome_text variable
    welcome_text = welcome_text_elt.text

    # using assert check that the expected text matches the text on the site page
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # waiting to evaluate the results of passing the script
    time.sleep(5)
    # close the browser after all manipulations
    browser.quit() 
