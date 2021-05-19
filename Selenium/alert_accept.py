from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    button1 = browser.find_element_by_class_name('btn')
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    time.sleep(1)
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(str(y))
    button = browser.find_element_by_class_name('btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
