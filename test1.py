from selenium import webdriver
from selenium.webdriver.common.by import By
 # Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()
# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')
# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.NAME, value='username')
username.send_keys('j213f0ab')
# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.ID, value='password')
password.send_keys('XEC134jt')
#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button=browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
#Нажимаем на кнопку входа
button.click()
# Закрываем браузер
browser.close()
