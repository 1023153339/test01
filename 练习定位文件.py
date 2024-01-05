import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#访问网址
driver.get("https://www.baidu.com/index.htm")
# #通过classname找到输入框输入hha
# driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("hha")
# #通过ID定位，点击
# driver.find_element(By.ID,"su").click()
# driver.find_elements(By.PARTIAL_LINK_TEXT,"闻")[0].click()
# time.sleep(5)
# for i in driver.find_elements(By.TAG_NAME,"a"):
#     print(i.text)
time.sleep(5)
