from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome(r'C:\chromedriver.exe')
 
driver.implicitly_wait(3)
 
driver.get('https://www.dbpia.co.kr/')
 
elm = driver.find_elements(By.ID, 'keyword')[0]
elm.send_keys('독일의')
 
btn_elm = driver.find_elements(By.CLASS_NAME, 'btnSearch')[0]
btn_elm.click()
 
sleep(10)
 
driver.quit()


