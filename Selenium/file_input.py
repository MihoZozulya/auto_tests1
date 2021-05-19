from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_name('firstname')
    element1.send_keys("Вася")
    # time.sleep(1)

    element2 = browser.find_element_by_name('lastname')
    element2.send_keys("Пупкин")
    # time.sleep(1)

    element3 = browser.find_element_by_name('email')
    element3.send_keys("vasyapupkin@mail.com")
    # time.sleep(1)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element4 = browser.find_element_by_name('file')
    element4.send_keys(file_path)


    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
