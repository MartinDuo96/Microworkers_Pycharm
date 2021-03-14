from selenium import webdriver
import time
import getId

api_key = 'AIzaSyBK064kZLO0ov7N9aTFAMhwXb-u0WYJIQE'


login_name = 'ray.ackermann1@gmail.com'
password = 'koenigss04'

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
url = 'https://www.youtube.de/'
driver.get(url)
time.sleep(1)
driver.find_element_by_id('action-button').click()  # search for button
getId.save_clipboard(login_name)
getId.keyboard_ctrl_v()
driver.find_element_by_id('identifierNext').click()