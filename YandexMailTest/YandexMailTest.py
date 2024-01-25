import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()  
driver.get('https://mail.yandex.ru/');
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div/div/header/div[1]/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/span/input').send_keys("login")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[2]/div[1]/span/input').send_keys("pass")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/div[1]/button').click()
time.sleep(3)
driver.quit()