import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get('https://www.iviewui.com/view-ui-plus/component/form/date-picker')
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]').send_keys("2024-01-05")
driver.find_elements(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys("2024-01-18 - 2024-02-12")

time.sleep(2)
driver.quit()