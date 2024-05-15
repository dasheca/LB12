import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Запускаем браузер
browser = webdriver.Chrome()
# Переходим на сайт goldapple.ru
browser.get('https://goldapple.ru/')
# Находим кнопку-иконку "Личный кабинет" и нажимаем на нее
personal_cabinet_button = browser.find_element(By.XPATH, '//button[@aria-label="Личный кабинет"]')
personal_cabinet_button.click()
# Ждем 2 секунды для открытия формы авторизации
time.sleep(2)
# Находим поле для ввода номера телефона и вводим номер
phone_input = browser.find_element(By.NAME, 'phone')
phone_input.send_keys('9924057452')
# Находим кнопку "Получить код" и нажимаем на нее
get_code_button = browser.find_element(By.XPATH, '//button[contains(text(), "Получить код")]')
get_code_button.click()
# Ждем 60 секунд
time.sleep(60)
# Закрываем браузер
browser.close()