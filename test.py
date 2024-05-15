from selenium import webdriver
# Получаем в переменную browser указатель на браузер
# В новых версиях можно использовать webdriver.Chrome()
browser=webdriver.Chrome()
# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')
# Закрываем браузер
browser.close()
