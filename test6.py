import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Запускаем браузер
browser = webdriver.Chrome()
# Переходим на сайт и авторизуемся
browser.get('https://goldapple.ru/')
# Нажатие на кнопку личного кабинета
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
# Ждем 3 секунды для загрузки страницы и авторизации
time.sleep(3)
# Переходим на страницу каталога товаров
catalog_button = browser.find_element(By.XPATH, '//button[@aria-label="Каталог товаров"]')
catalog_button.click()
# Ждем 2 секунды для загрузки страницы каталога товаров
time.sleep(2)
# Выбираем товар в каталоге (предполагаем, что это первый товар на странице)
product_card = browser.find_element(By.XPATH, '//div[@class="product-card"][1]')
product_card.click()
# Ждем 2 секунды для загрузки страницы товара
time.sleep(2)
# Нажимаем на кнопку-иконку "Сердце" для добавления товара в избранное
favorite_button = browser.find_element(By.XPATH, '//button[@aria-label="Добавить в избранное"]')
favorite_button.click()
# Ждем 2 секунды для добавления товара в избранное
time.sleep(2)
# Переходим на страницу избранное
favorite_page_button = browser.find_element(By.XPATH, '//button[@aria-label="Избранное"]')
favorite_page_button.click()
# Ждем 2 секунды для загрузки страницы избранного
time.sleep(2)
# Закрываем браузер
browser.close()
