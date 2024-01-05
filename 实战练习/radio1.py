import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.iviewui.com/view-ui-plus/component/form/radio')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//div/div[1]/div/label[@class='ivu-radio-wrapper ivu-radio-group-item ivu-radio-default']/span[text()='Android']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div/div[1]/div/label[@class='ivu-radio-wrapper ivu-radio-group-item ivu-radio-default']/span[text()='Windows']").click()
time.sleep(3)
driver.quit()

