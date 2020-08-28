from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
sleep(2)
# 鼠标悬停
el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(el).perform()
sleep(1)
# 点击悬停后显示出来的元素
driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()

sleep(3)
driver.quit()