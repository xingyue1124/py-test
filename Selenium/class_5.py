from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/')
driver.find_element_by_xpath('//a[text()="登录"]').click()
driver.find_element_by_xpath('//input[@name="accounts"]').send_keys('666666')
driver.find_element_by_xpath('//input[@name="pwd"]').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
# 用于校验元素是否登录成功（通过显式等待）
try:
    WebDriverWait(driver, 10, 0.5).until(
        lambda el: driver.find_element_by_xpath('//a[text()="退出"]'), message='登录失败')
except Exception as e:
    print('登录失败，信息不正确：{0}'.format(e))

sleep(5)
driver.quit()