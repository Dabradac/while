import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)

browser.get('https://testpages.herokuapp.com/styled/drag-drop-javascript.html') # инициализация браузера
element = browser.find_element(By.CSS_SELECTOR, '#draggable2').send_keys('') # отправка клавиш на элемент
browser.find_element(By.CSS_SELECTOR, '#draggable2').click() # клик по элементу
browser.find_element(By.CSS_SELECTOR, '#draggable2').text   # поиск текста в элементе
browser.find_element(By.CSS_SELECTOR, ' ') # поиск элемента
drop = browser.find_element(By.CSS_SELECTOR, '#droppable1') # задаем переменной значение элемента
action = ActionChains(browser)  # инициализация цепочки действий
action.click_and_hold(element) # клик и удержание
action.move_to_element(drop) # перемещение на элемент
action.drag_and_drop(element,drag,drop) # drag and drop
action.context_click() # клик правой кнопкой мыши
action.release()# отпустить кнопку мыши
action.perform() # подтверждение

