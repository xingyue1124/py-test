# from selenium import webdriver
# from  time import sleep
# # 显式等待的模块的调用
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.get('http://39.98.138.157/shopxo/index.php')
# # 设置显式等待，等待登录元素出现，然后再进行后续的操作。显式等待需要设置等待的时间
# # driver对象是显式等待中必须传递的driver参数，第二个参数(timeout)是最大等待时间，第三个参数是查看频率，默认是0.5的频率
# el = WebDriverWait(driver, 5, 0.5).until(
#     lambda el1: driver.find_element_by_xpath('//a[text()="登录"]'), message='元素定位失败')
# el.click()
# driver.find_element_by_xpath('//input[@name="accounts"]').send_keys('666666')
# driver.find_element_by_xpath('//input[@name="pwd"]').send_keys('111111')
# driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
#
# sleep(3)
# driver.quit()


from selenium import webdriver
# 显式等待的模块的调用
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome()
# 设置隐式等待
driver.implicitly_wait(5)
driver.get('http://39.98.138.157/shopxo/index.php')
# 设置显式等待，等待登录元素出现，然后再进行后续的操作。显式等待需要设置等待的时间
# driver对象是显式等待中必须传递的driver参数，第二个参数是最大等待时间，第三个参数是查看频率，默认是0.5的频率
el = WebDriverWait(driver, 5, 0.5).until(
    lambda el1: driver.find_element_by_xpath('//a[text()="登录"]'), message='元素定位失败')
el.click()
driver.find_element_by_xpath('//input[@name="accounts"]').send_keys('666666')
driver.find_element_by_xpath('//input[@name="pwd"]').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
# 退出
WebDriverWait(driver, 10, 0.5).until(
    lambda el1: driver.find_element_by_xpath('//a[text()="退出"]'), message='未成功登录')
# 强制等待
sleep(5)
driver.quit()
