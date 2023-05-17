import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)



browser.get('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjK5pjd8vz-AhVgQvEDHeTrBFoQPAgI')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('autotest')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[7]/center/input[1]').click()
element = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/g-section-with-header/div[1]/title-with-lhs-icon/a/div[3]/h3').text
assert element == 'Картинки по запросу autotest'

