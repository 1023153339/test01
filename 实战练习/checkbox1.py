import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get('https://www.iviewui.com/view-ui-plus/component/form/checkbox')
driver.find_element(By.XPATH,"//div/div[1]/div/label[4]/span[2]/span[text()='Snapchat']").click()


time.sleep(2)
driver.quit()