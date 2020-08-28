from selenium import webdriver
# 强制等待的两种导入方式
from time import sleep
import time

driver = webdriver.Chrome()
driver.get('http://39.98.138.157/shopxo/index.php')
time.sleep(2)
driver.find_element_by_xpath('//a[text()="登录"]').click()
sleep(2)
driver.find_element_by_xpath('//input[@name="accounts"]').send_keys('666666')
driver.find_element_by_xpath('//input[@name="pwd"]').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

sleep(3)
driver.quit()