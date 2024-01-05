import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import utils.get_filepath

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://baidu.com")
# driver.find_element(By.XPATH,"/html/body/div/div/div[3]/a").click()#绝对路径
# driver.find_element(By.XPATH,"//div[@id='wrapper']/div/div[@id='s-top-left']/a[1]").click()#相对路径id定位且第一个元素
# driver.find_element(By.XPATH,"//div[@id='wrapper']/div/div[@class='s-top-left-new s-isindex-wrap']/a[last()]").click()#相对路径class定位最后一个元素
# driver.find_element(By.XPATH,"//div[@id='head']/div/div[@class='mnav s-top-more-btn']/a[@name='tj_briicon']").click()#name属性定位
# driver.find_element(By.XPATH,"//div[@id='head']/div/div[@class='mnav s-top-more-btn']/a[text()='更多']").click()#文本等于
# driver.find_element(By.XPATH,"//div[@id='head']/div/div[@class='mnav s-top-more-btn']/a[contains(text(),'更')]").click()#文本包含
# driver.find_element(By.XPATH,"//div[@id='wrapper']/div/div[@id='s-top-left']/a[2]/following-sibling::a[2]").click()#同级弟弟
print(utils.get_filepath.file_11())
# driver.find_element(By.XPATH,"//div[@id='wrapper']/div/div[@id='s-top-left']/a[2]/preceding-sibling::a").click()#同级哥哥
time.sleep(5)

driver.quit()