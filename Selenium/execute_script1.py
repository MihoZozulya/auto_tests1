from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    #time.sleep(1)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    #time.sleep(1)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    #time.sleep(1)

    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    #time.sleep(1)

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    #time.sleep(1)

    button = browser.find_element_by_class_name('btn')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
