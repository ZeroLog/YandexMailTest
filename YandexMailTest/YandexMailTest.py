import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# settings
log = "log"
passw = "pass"
sitetest = "https://mail.yandex.ru/"
file_path = r"C:\Users\ZeroLog\Documents\testlog\test.log"

driver = webdriver.Chrome()
driver.get(sitetest)


def to_file(text):
    try:
        with open(file_path, 'a') as file:
            file.write(text + '\n')
        print(f"Text appended to {file_path}")
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write(text + '\n')
        print(f"File {file_path} created, and text appended")

# Авторизация в сервисе

def login():
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/div/header/div[1]/div[2]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/span/input').send_keys(log)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[2]/div[1]/span/input').send_keys(passw)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/div[1]/button').click()
    time.sleep(3)
    user_account_element = driver.find_element(By.CLASS_NAME, 'user-account__name')
    if user_account_element.text == log:
        to_file("Test 1 passed")
    else:
        to_file("Test 1 failed")

# Отправление письма








# login()


driver.quit()
