import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/cascader")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="base"]/div/div[@class="ivu-card-body"]/div/div/div[1]/div[1]/div[1]/input[@class="ivu-input ivu-input-default"]').click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/span/ul/li[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/span/span/ul/li[1]").click()
time.sleep(2)
driver.quit()
