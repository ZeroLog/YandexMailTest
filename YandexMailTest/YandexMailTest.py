import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# settings
log = "login"
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

# Authorization testing

def login():
    to_file("Test 1 start")
    time.sleep(15)
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

# Sending a letter

def send_mail():
    to_file("Test 2 start")
    email_subject = "test"
    driver.find_element(By.CLASS_NAME, "qa-LeftColumn-ComposeButton").click()
    time.sleep(2)
    driver.find_element(By.ID, "compose-field-1").send_keys(log)
    driver.find_element(By.ID, "compose-field-subject-4").send_keys(email_subject)
    driver.find_element(By.CLASS_NAME, "cke_wysiwyg_div").send_keys("test2")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.Button2.Button2_view_action.Button2_size_l').click()
    time.sleep(5)
    email_xpath = f'//span[@title="{email_subject}"]'
    try:
        email_element = driver.find_element(By.XPATH, email_xpath)
        to_file("Test 2 passed")
    except:
        to_file("Test 2 failed")
        
        
#Creating a folder

def creating_folder():
    to_file("Test 3 start")
    driver.find_element(By.CSS_SELECTOR, '.Button2.Button2_view_clear.Button2_size_xs.qa-LeftColumn-AddFolderButton.AddItemButton-m__root--19X88').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "nb-input").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, '.b-popup__confirm .nb-button._nb-small-button._init.ns-action[data-dialog-action="dialog.submit"]').click()
    time.sleep(3)
    folder_xpath ='//span[text()="test"]/ancestor::div[contains(@class, "qa-LeftColumn-FolderNodeContent")]'
    try:
        folder_element = driver.find_element(By.XPATH, folder_xpath)
        to_file("Test 3 passed")
    except:
        to_file("Test 3 failed")
        
#Creating a test button

def mov_letter():
     
     to_file("Test 4 start")
     email_xpath = f'//span[@title="test"]'
     time.sleep(3)
     driver.find_element(By.XPATH, email_xpath).click()
     time.sleep(2)
     driver.find_element(By.CLASS_NAME, 'ns-view-toolbar-button-toolbar-settings').click()
     time.sleep(3)
     driver.find_element(By.CLASS_NAME, "js-toolbar-settings-button-infolder").click()
     time.sleep(2)
     select_element = driver.find_element(By.NAME, "folder")
     time.sleep(2)
     select = Select(select_element)
     select.select_by_visible_text("test")
     time.sleep(1)
     driver.find_element(By.CSS_SELECTOR, 'button[data-click-action="toolbar.settings.submitButtonOptions"]').click()
     time.sleep(1)
     driver.find_element(By.CLASS_NAME, "nb-button._nb-action-button._init.js-clickable.js-toolbar-settings-control.js-toolbar-settings-apply.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()
     time.sleep(2)
     driver.refresh()
     time.sleep(3)
     try:
        test_element = driver.find_elements(By.XPATH, '//div[@class="mail-Toolbar-Popup-Item" and text()="test"]')
        to_file("Test 4 passed")

     except:
        to_file("Test 4 failed")


     


login()
mov_letter()
send_mail()
creating_folder()

driver.quit()
