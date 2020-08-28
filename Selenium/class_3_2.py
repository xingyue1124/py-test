from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://music.163.com')
driver.find_element_by_xpath('//a[text()="登录"]').click()
driver.find_element_by_xpath('//a[text()="选择其他登录模式"]').click()
driver.find_element_by_xpath('//*[@id="j-official-terms"]').click()
driver.find_element_by_xpath('//*[text()="QQ登录"]').click()
handles = driver.window_handles
# 切换到QQ登录页面
driver.switch_to.window(handles[1])
sleep(2)

# iframe元素。如果被操作元素是在iframe中，则无法直接进行定位，需要先切换到iframe再来操作元素
# 切换iframe，默认可以通过id和name进行直接切换，如果没有，就用定位元素进行切换
driver.switch_to.frame('ptlogin_iframe')
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="ptlogin_iframe"]')) 元素定位切换
driver.find_element_by_xpath('//*[@id="qlogin_list"]/a[1]').click()
# 从iframe中切换回原来的页面,才可以操作其他元素
driver.switch_to.default_content()
sleep(2)

# 切换句柄
driver.switch_to.window(handles[0])
sleep(2)
driver.find_element_by_xpath('//*[@id="p"]').send_keys('123456')

sleep(3)
driver.quit()