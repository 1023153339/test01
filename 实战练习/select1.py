import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/select")
# 使用html的select方法
# select = Select(driver.find_element(By.ID,"s3Id"))
# select.select_by_value("o2val")#下标用（0）
# 使用其他方法
time.sleep(2)
driver.find_element(By.XPATH,'//div/div[3]/div/div[1]/div/span').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div/div[3]/div/div[2]/ul[2]/li[3]').click()
time.sleep(2)
driver.quit()