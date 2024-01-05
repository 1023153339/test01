import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("hha")#ID
# driver.find_element(By.CSS_SELECTOR,".s_ipt").send_keys("11")#类
# driver.find_elements(By.CSS_SELECTOR,'[autocomplete="off"]')[0].send_keys("2")#属性名
# driver.find_element(By.CSS_SELECTOR,"input.text").send_keys()#组合选择器 标签.属性描述
# driver.find_element(By.CSS_SELECTOR, "input").send_keys("hahh")#查找input标签
# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("ID定位")
# driver.find_element(By.CSS_SELECTOR,".s_ipt").send_keys("class定位")
# driver.find_element(By.CSS_SELECTOR,"[name='wd']").send_keys("name属性定位")
# driver.find_element(By.CSS_SELECTOR,"a[href='http://www.baidu.com/more/']").click()#超链接定位
# driver.find_element(By.CSS_SELECTOR,"a[href*='//www.baidu.com/more']").click()#超链接定位模糊搜索包含
# driver.find_element(By.CSS_SELECTOR,"a[href^='http://www.baidu.com/m']").click()#匹配开头
# driver.find_element(By.CSS_SELECTOR,"a[href$='www.baidu.com/more/']").click()#匹配结尾
# driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys("1")#组合查询. class
# driver.find_element(By.CSS_SELECTOR,"div#wrapper>div#head>div#s-top-left>a:nth-child(3)").click()#父子级查询
# driver.find_element(By.CSS_SELECTOR,"div#wrapper>div#head>div#s-top-left>a:first-child").click()#父子级查询查找第一个
# driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a:last-child").click()#父子级查询查找最后一个
time.sleep(5)


driver.quit()
