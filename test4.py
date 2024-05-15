import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Запускаем браузер
browser = webdriver.Chrome()
# Переходим на сайт
browser.get('https://goldapple.ru/')
# Находим поле для ввода запроса и вводим текст запроса
search_input = browser.find_element(By.CLASS_NAME, 'js-header-search-input')
search_input.send_keys('гель для бровей')
# Находим кнопку для отправки запроса и нажимаем на нее
submit_button = browser.find_element(By.CLASS_NAME, 'js-header-search-submit')
submit_button.click()
# Ждем 60 секунд
time.sleep(60)
# Закрываем браузер
browser.close()